from typing import Optional, List
from pydantic import BaseModel, Field
from datetime import datetime

class UserCompanyBase(BaseModel):
    id: Optional[int] = None
    user_id: int
    company_id: int
    joined_at: Optional[datetime] = None
    granted_by: Optional[int] = None
    granted_at: Optional[datetime] = Field(default_factory=datetime.now)
    created_at: Optional[datetime] = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = None

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "company_id": self.company_id,
            "joined_at": self.joined_at.isoformat() if self.joined_at else None,
            "granted_by": self.granted_by,
            "granted_at": self.granted_at.isoformat() if self.granted_at else None,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

    class Config:
        orm_mode = True


class UserCompanyResponse(BaseModel):
    status_code: int
    data: Optional[UserCompanyBase] = None


class UserCompanyListResponse(BaseModel):
    status_code: int
    data: List[UserCompanyBase] = Field(default_factory=list)
