from typing import Optional, List
from pydantic import BaseModel, Field
from datetime import datetime

class CompanyGroupBase(BaseModel):
    id: Optional[int] = None
    company_id: int
    granted_by: Optional[int] = None
    granted_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    def to_dict(self):
        return {
            "id": self.id,
            "company_id": self.company_id,
            "granted_by": self.granted_by,
            "granted_at": self.granted_at.isoformat() if self.granted_at else None,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

    class Config:
        from_attributes = True


class CompanyGroupResponse(BaseModel):
    status_code: int
    data: Optional[CompanyGroupBase] = None


class CompanyGroupListResponse(BaseModel):
    status_code: int
    data: List[CompanyGroupBase] = []
