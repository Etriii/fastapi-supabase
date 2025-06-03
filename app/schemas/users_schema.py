from typing import Optional, List
from pydantic import BaseModel, Field
from datetime import datetime

class UserBase(BaseModel):
    id: Optional[int] = None
    username: str
    email: str
    password_hash: str
    created_at: Optional[datetime] = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = None

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "password_hash": self.password_hash,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

    class Config:
        orm_mode = True


class UserResponse(BaseModel):
    status_code: int
    data: Optional[UserBase] = None


class UserListResponse(BaseModel):
    status_code: int
    data: List[UserBase] = Field(default_factory=list)
