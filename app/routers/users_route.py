from datetime import datetime
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select

from .. import models as db_models
from ..schemas import user_schema
from ..utils.schemas import status_response_schema
from ..db import get_db

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/", response_model=user_schema.UserListResponse)
def get_all_users(
    db: Session = Depends(get_db),
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
):
    try:
        users_query = select(db_models.User).join().offset(offset).limit(limit)
        users = db.exec(users_query).all()
        return user_schema.UserListResponse(status_code=200, data=users)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {e}")


@router.get("/{user_id}", response_model=user_schema.UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    try:
        user = db.get(db_models.User, user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user_schema.UserResponse(status_code=200, data=user)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {e}")


@router.post("/", response_model=user_schema.UserResponse)
def create_user(user: user_schema.UserBase, db: Session = Depends(get_db)):
    try:
        user.created_at = datetime.now()
        user.email_verified_at = user.email_verified_at or datetime.now()
        user_data = db_models.User(**user.model_dump(exclude_unset=True))
        db.add(user_data)
        db.commit()
        db.refresh(user_data)
        return user_schema.UserResponse(status_code=201, data=user_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {e}")


@router.put("/{user_id}", response_model=user_schema.UserResponse)
def update_user(user_id: int, user: user_schema.UserBase, db: Session = Depends(get_db)):
    try:
        db_user = db.get(db_models.User, user_id)
        if not db_user:
            raise HTTPException(status_code=404, detail="User not found")

        updated_data = db_models.User.model_validate(user)
        db_user.sqlmodel_update(updated_data)
        db_user.updated_at = datetime.now()

        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return user_schema.UserResponse(status_code=200, data=db_user)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {e}")


@router.delete("/{user_id}", response_model=status_response_schema.StatusResponse)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    try:
        db_user = db.get(db_models.User, user_id)
        if not db_user:
            raise HTTPException(status_code=404, detail="User not found")

        db.delete(db_user)
        db.commit()
        return status_response_schema.StatusResponse(status_code=200, data=True)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {e}")
