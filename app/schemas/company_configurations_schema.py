from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field
from datetime import datetime

class CompanyConfigurationBase(BaseModel):
    id: Optional[int] = None
    company_id: int
    users_allowed: int
    licensed_expiration_date: Optional[datetime] = None
    custom_settings: Optional[Dict[str, Any]] = None
    created_at: Optional[datetime] = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = None

    def to_dict(self):
        return {
            "id": self.id,
            "company_id": self.company_id,
            "users_allowed": self.users_allowed,
            "licensed_expiration_date": self.licensed_expiration_date.isoformat() if self.licensed_expiration_date else None,
            "custom_settings": self.custom_settings,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

    class Config:
        orm_mode = True


class CompanyConfigurationResponse(BaseModel):
    status_code: int
    data: Optional[CompanyConfigurationBase] = None


class CompanyConfigurationListResponse(BaseModel):
    status_code: int
    data: List[CompanyConfigurationBase] = Field(default_factory=list)
