from pydantic import BaseModel

class StatusResponse(BaseModel):
    status_code: int
    data: bool