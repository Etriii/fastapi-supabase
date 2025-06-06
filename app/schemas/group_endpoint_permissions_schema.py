from typing import Optional, List
from pydantic import BaseModel, Field
from datetime import datetime


class GroupEndpointPermissionBase(BaseModel):
    id: Optional[int] = None
    group_id: int
    permission_id: int
    endpoint_id: int
    granted_by: Optional[int] = None
    granted_at: Optional[datetime] = None
    can_create: bool = False
    can_read: bool = False
    can_update: bool = False
    can_delete: bool = False
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    def to_dict(self):
        return {
            "id": self.id,
            "group_id": self.group_id,
            "permission_id": self.permission_id,
            "endpoint_id": self.endpoint_id,
            "granted_by": self.granted_by,
            "granted_at": self.granted_at.isoformat() if self.granted_at else None,
            "can_create": self.can_create,
            "can_read": self.can_read,
            "can_update": self.can_update,
            "can_delete": self.can_delete,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

    class Config:
        from_attributes = True


class GroupEndpointPermissionResponse(BaseModel):
    status_code: int
    data: Optional[GroupEndpointPermissionBase] = None


class GroupEndpointPermissionListResponse(BaseModel):
    status_code: int
    data: List[GroupEndpointPermissionBase] = []
