from typing import Optional, List
from pydantic import BaseModel, Field
from datetime import datetime

class CompanyBase(BaseModel):
    id: Optional[int] = None
    name: str
    short_name: str
    logo_url: str
    created_at: Optional[datetime] = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = None

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "short_name": self.short_name,
            "logo_url": self.logo_url,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

    class Config:
        orm_mode = True


class CompanyResponse(BaseModel):
    status_code: int
    data: Optional[CompanyBase] = None


class CompanyListResponse(BaseModel):
    status_code: int
    data: List[CompanyBase] = Field(default_factory=list)
