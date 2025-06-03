from typing import Optional, List
from pydantic import BaseModel, Field
from datetime import datetime

class PermissionBase(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    created_at: Optional[datetime] = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = None

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

    class Config:
        orm_mode = True


class PermissionResponse(BaseModel):
    status_code: int
    data: Optional[PermissionBase] = None


class PermissionListResponse(BaseModel):
    status_code: int
    data: List[PermissionBase] = Field(default_factory=list)
