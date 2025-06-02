from sqlmodel import Field, SQLModel
from datetime import datetime
from enum import Enum

# Define an Enum for HTTP methods for the Endpoints table
class HttpMethod(str, Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"
    HEAD = "HEAD"
    OPTIONS = "OPTIONS"


class Group(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(max_length=255)
    description: str = Field(default=None, max_length=1024)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default=None)


class Permission(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(max_length=255)
    description: str = Field(default=None, max_length=1024)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default=None)


class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    username: str = Field(max_length=255, unique=True)
    email: str = Field(max_length=255, unique=True)
    password_hash: str = Field(max_length=255)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default=None)


class UserGroup(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id", index=True)
    group_id: int = Field(foreign_key="groups.id", index=True)
    granted_by: int = Field(default=None, foreign_key="users.id", index=True)
    granted_at: datetime = Field(default_factory=datetime.now)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default=None)


class UserCompany(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id", index=True)
    company_id: int = Field(foreign_key="companies.id", index=True)
    joined_at: datetime = Field(default=None)
    granted_by: int = Field(default=None, foreign_key="users.id", index=True)
    granted_at: datetime = Field(default_factory=datetime.now)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default=None)


class CompanyConfiguration(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    company_id: int = Field(foreign_key="companies.id", unique=True, index=True)
    users_allowed: int
    licensed_expiration_date: datetime = Field(default=None)
    custom_settings: dict = Field(default=None)  # Using dict for JSON type
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default=None)


class Company(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(max_length=255, unique=True)
    short_name: str = Field(default=None, max_length=50)
    logo_url: str = Field(default=None, max_length=512)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default=None)


class CompanyGroup(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    company_id: int = Field(foreign_key="companies.id", unique=True, index=True)
    granted_by: int = Field(default=None, foreign_key="users.id", index=True)
    granted_at: datetime = Field(default_factory=datetime.now)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default=None)


class GroupEndpointPermission(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    group_id: int = Field(foreign_key="groups.id", index=True)
    permission_id: int = Field(foreign_key="permissions.id", index=True)
    endpoint_id: int = Field(foreign_key="endpoints.id", index=True)
    granted_by: int = Field(default=None, foreign_key="users.id", index=True)
    granted_at: datetime = Field(default_factory=datetime.now)
    can_create: bool = Field(default=False)
    can_read: bool = Field(default=False)
    can_update: bool = Field(default=False)
    can_delete: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default=None)


class Endpoint(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    route: str = Field(max_length=255)
    method: HttpMethod  # Using the HttpMethod Enum
    description: str = Field(default=None, max_length=1024)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default=None)


class GroupPermission(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    group_id: int = Field(foreign_key="groups.id", index=True)
    permission_id: int = Field(foreign_key="permissions.id", index=True)
    granted_by: int = Field(default=None, foreign_key="users.id", index=True)
    granted_at: datetime = Field(default_factory=datetime.now)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default=None)
