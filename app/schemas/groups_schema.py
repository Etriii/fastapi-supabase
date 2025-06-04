from typing import Optional, List
from pydantic import BaseModel, Field
from datetime import datetime

class GroupBase(BaseModel):
    id: Optional[int] = None
    name: str
    description: str
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
        from_attributes = True


class GroupResponse(BaseModel):
    status_code: int
    data: Optional[GroupBase] = None


class GroupListResponse(BaseModel):
    status_code: int
    data: List[GroupBase] = Field(default_factory=list)
