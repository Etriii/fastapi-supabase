from sqlmodel import Field, SQLModel
from sqlalchemy import Column, JSON, String, DateTime, Enum as SAEnum
from datetime import datetime
from enum import Enum
from typing import Optional


# Define an Enum for HTTP methods for the Endpoints table
class HttpMethod(str, Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"
    HEAD = "HEAD"
    OPTIONS = "OPTIONS"


# class Roles(SQLModel, table=True):
#     __tablename__ = "roles"
#     id: int = Field(default=None, primary_key=True)

# class Roles(SQLModel, table=True):
#     __tablename__ = "user_roles"
#     id: int = Field(default=None, primary_key=True)


class Group(SQLModel, table=True):
    __tablename__ = "groups"
    id: int = Field(default=None, primary_key=True)
    name: str = Field(sa_column=Column(String(255), unique=True, index=True))
    description: str = Field(sa_column=Column(String(1024), unique=True, index=True))
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = Field(
        default=None, sa_column=Column(DateTime, nullable=True)
    )


class Permission(SQLModel, table=True):
    __tablename__ = "permissions"
    id: int = Field(default=None, primary_key=True)
    name: str = Field(sa_column=Column(String(255), unique=True, index=True))
    description: str = Field(sa_column=Column(String(1024), index=True))
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = Field(
        default=None, sa_column=Column(DateTime, nullable=True)
    )


class User(SQLModel, table=True):
    __tablename__ = "users"
    id: int = Field(default=None, primary_key=True)
    username: str = Field(sa_column=Column(String(255), unique=True, index=True))
    email: str = Field(sa_column=Column(String(255), unique=True, index=True))
    email_verified_at: Optional[datetime] = Field(
        default=None, sa_column=Column(DateTime, nullable=True)
    )
    password_hash: str = Field(sa_column=Column(String(1024)))
    profile: str = Field(sa_column=Column(String(255), nullable=True))
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = Field(
        default=None, sa_column=Column(DateTime, nullable=True)
    )


class UserCompany(SQLModel, table=True):
    __tablename__ = "user_companies"
    id: int = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id", index=True)
    group_id: int = Field(foreign_key="groups.id", index=True)
    company_id: int = Field(foreign_key="companies.id", index=True)
    granted_by: int = Field(default=None, foreign_key="users.id", index=True)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = Field(
        default=None, sa_column=Column(DateTime, nullable=True)
    )


class CustomUISettings(SQLModel, table=True):
    __tablename__ = "custom_ui_settings"
    id: int = Field(default=None, primary_key=True)
    theme: str = Field(sa_column=Column(String(100)))
    primary_color: str = Field(sa_column=Column(String(50)))
    secondary_color: str = Field(sa_column=Column(String(50)))
    accent_color: str = Field(sa_column=Column(String(50)))
    timezone: str = Field(sa_column=Column(String(50)))
    default_language: str = Field(sa_column=Column(String(50)))


class CompanyConfiguration(SQLModel, table=True):
    __tablename__ = "company_configurations"
    id: int = Field(default=None, primary_key=True)
    company_id: int = Field(foreign_key="companies.id", unique=True, index=True)
    users_allowed: int
    licensed_expiration_date: datetime = Field(default=None)
    custom_settings_id: int = Field(
        foreign_key="custom_ui_settings.id", unique=True, index=True
    )
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = Field(
        default=None, sa_column=Column(DateTime, nullable=True)
    )


class Company(SQLModel, table=True):
    __tablename__ = "companies"
    id: int = Field(default=None, primary_key=True)
    name: str = Field(sa_column=Column(String(255), unique=True, index=True))
    short_name: str = Field(sa_column=Column(String(50), unique=True, index=True))
    logo_url: str = Field(sa_column=Column(String(500)))
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = Field(
        default=None, sa_column=Column(DateTime, nullable=True)
    )


class CompanyGroup(SQLModel, table=True):
    __tablename__ = "company_groups"
    id: int = Field(default=None, primary_key=True)
    company_id: int = Field(foreign_key="companies.id", unique=True, index=True)
    granted_by: int = Field(default=None, foreign_key="users.id", index=True)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = Field(
        default=None, sa_column=Column(DateTime, nullable=True)
    )


class GroupEndpointPermission(SQLModel, table=True):
    __tablename__ = "group_endpoint_permissions"
    id: int = Field(default=None, primary_key=True)
    group_id: int = Field(foreign_key="groups.id", index=True)
    permission_id: int = Field(foreign_key="permissions.id", index=True)
    endpoint_id: int = Field(foreign_key="endpoints.id", index=True)
    granted_by: int = Field(default=None, foreign_key="users.id", index=True)
    can_create: bool = Field(default=False)
    can_read: bool = Field(default=False)
    can_update: bool = Field(default=False)
    can_delete: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = Field(
        default=None, sa_column=Column(DateTime, nullable=True)
    )


class Endpoint(SQLModel, table=True):
    __tablename__ = "endpoints"
    id: int = Field(default=None, primary_key=True)
    route: str = Field(sa_column=Column(String(255), index=True))
    method: HttpMethod = Field(
        sa_column=Column(SAEnum(HttpMethod, name="http_method_enum"), index=True)
    )
    description: str = Field(sa_column=Column(String(1024)))
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = Field(
        default=None, sa_column=Column(DateTime, nullable=True)
    )


class GroupPermission(SQLModel, table=True):
    __tablename__ = "group_permissions"
    id: int = Field(default=None, primary_key=True)
    group_id: int = Field(foreign_key="groups.id", index=True)
    permission_id: int = Field(foreign_key="permissions.id", index=True)
    granted_by: int = Field(default=None, foreign_key="users.id", index=True)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = Field(
        default=None, sa_column=Column(DateTime, nullable=True)
    )
