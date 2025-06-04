from typing import Optional, List
from pydantic import BaseModel, Field
from datetime import datetime

class GroupPermissionBase(BaseModel):
    id: Optional[int] = None
    group_id: int
    permission_id: int
    granted_by: Optional[int] = None
    granted_at: Optional[datetime] = Field(default_factory=datetime.now)
    created_at: Optional[datetime] = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = None

    def to_dict(self):
        return {
            "id": self.id,
            "group_id": self.group_id,
            "permission_id": self.permission_id,
            "granted_by": self.granted_by,
            "granted_at": self.granted_at.isoformat() if self.granted_at else None,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

    class Config:
        from_attributes = True

class GroupPermissionResponse(BaseModel):
    status_code: int
    data: Optional[GroupPermissionBase] = None

class GroupPermissionListResponse(BaseModel):
    status_code: int
    data: List[GroupPermissionBase] = Field(default_factory=list)
