from typing import Optional, List
from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum

class HttpMethod(str, Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"
    OPTIONS = "OPTIONS"
    HEAD = "HEAD"

class EndpointBase(BaseModel):
    id: Optional[int] = None
    route: str
    method: HttpMethod
    description: str
    created_at: Optional[datetime] = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = None

    def to_dict(self):
        return {
            "id": self.id,
            "route": self.route,
            "method": self.method.value if self.method else None,
            "description": self.description,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

    class Config:
        from_attributes = True

class EndpointResponse(BaseModel):
    status_code: int
    data: Optional[EndpointBase] = None

class EndpointListResponse(BaseModel):
    status_code: int
    data: List[EndpointBase] = Field(default_factory=list)
