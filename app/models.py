from sqlmodel import Field, SQLModel
from sqlalchemy import Column, JSON, String, Enum as SAEnum
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
    __tablename__ = "groups"
    id: int = Field(default=None, primary_key=True)
    name: str = Field(sa_column=Column(String(255), unique=True, index=True))
    description: str = Field(sa_column=Column(String(1024), unique=True, index=True))
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default=None)


class Permission(SQLModel, table=True):
    __tablename__ = "permissions"
    id: int = Field(default=None, primary_key=True)
    name: str = Field(sa_column=Column(String(255), unique=True, index=True))
    description: str = Field(sa_column=Column(String(1024), index=True))
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default=None)


class User(SQLModel, table=True):
    __tablename__ = "users"
    id: int = Field(default=None, primary_key=True)
    username: str = Field(sa_column=Column(String(255), unique=True, index=True))
    email: str = Field(sa_column=Column(String(255), unique=True, index=True))
    password_hash: str = Field(sa_column=Column(String(1024)))
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default=None)


class UserGroup(SQLModel, table=True):
    __tablename__ = "user_groups"
    id: int = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id", index=True)
    group_id: int = Field(foreign_key="groups.id", index=True)
    granted_by: int = Field(default=None, foreign_key="users.id", index=True)
    granted_at: datetime = Field(default_factory=datetime.now)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default=None)


class UserCompany(SQLModel, table=True):
    __tablename__ = "user_companies"
    id: int = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id", index=True)
    company_id: int = Field(foreign_key="companies.id", index=True)
    joined_at: datetime = Field(default=None)
    granted_by: int = Field(default=None, foreign_key="users.id", index=True)
    granted_at: datetime = Field(default_factory=datetime.now)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default=None)


class CompanyConfiguration(SQLModel, table=True):
    __tablename__ = "company_configurations"
    id: int = Field(default=None, primary_key=True)
    company_id: int = Field(foreign_key="companies.id", unique=True, index=True)
    users_allowed: int
    licensed_expiration_date: datetime = Field(default=None)
    custom_settings: dict = Field(default=None, sa_column=Column(JSON))
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default=None)


class Company(SQLModel, table=True):
    __tablename__ = "companies"
    id: int = Field(default=None, primary_key=True)
    name: str = Field(sa_column=Column(String(255), unique=True, index=True))
    short_name: str = Field(sa_column=Column(String(50), unique=True, index=True))
    logo_url: str = Field(sa_column=Column(String(500)))
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default=None)


class CompanyGroup(SQLModel, table=True):
    __tablename__ = "company_groups"
    id: int = Field(default=None, primary_key=True)
    company_id: int = Field(foreign_key="companies.id", unique=True, index=True)
    granted_by: int = Field(default=None, foreign_key="users.id", index=True)
    granted_at: datetime = Field(default_factory=datetime.now)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default=None)


class GroupEndpointPermission(SQLModel, table=True):
    __tablename__ = "group_endpoint_permissions"
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
    __tablename__ = "endpoints"
    id: int = Field(default=None, primary_key=True)
    route: str = Field(sa_column=Column(String(255), index=True))
    method: HttpMethod = Field(sa_column=Column(SAEnum(HttpMethod, name="http_method_enum"), index=True))
    description: str = Field(sa_column=Column(String(1024)))
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default=None)


class GroupPermission(SQLModel, table=True):
    __tablename__ = "group_permissions"
    id: int = Field(default=None, primary_key=True)
    group_id: int = Field(foreign_key="groups.id", index=True)
    permission_id: int = Field(foreign_key="permissions.id", index=True)
    granted_by: int = Field(default=None, foreign_key="users.id", index=True)
    granted_at: datetime = Field(default_factory=datetime.now)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default=None)
