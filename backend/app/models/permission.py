import uuid
from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

if TYPE_CHECKING:
    from app.models.role_permission import RolePermission


class Permission(Base):
    __tablename__ = "permissions"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    permission_key: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
    )

    role_permissions: Mapped[list["RolePermission"]] = relationship(
        back_populates="permission",
    )