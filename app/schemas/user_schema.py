from typing import Optional, List
from pydantic import BaseModel, Field
from datetime import datetime
from app.models import User


class UserBase(BaseModel):
    id: Optional[int] = None
    username: str
    email: str
    email_verified_at: Optional[datetime] = None
    password_hash: str
    profile: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "email_verified_at": (
                self.email_verified_at.isoformat() if self.email_verified_at else None
            ),
            "password_hash": self.password_hash,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

    class Config:
        from_attributes = True


class UserResponse(BaseModel):
    status_code: int
    data: Optional[UserBase] = None


class UserListResponse(BaseModel):
    status_code: int
    data: List[UserBase] = []
