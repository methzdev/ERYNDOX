import uuid
from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

if TYPE_CHECKING:
    from app.models.workspace_member import WorkspaceMember
    from app.models.role_permission import RolePermission


class Role(Base):
    __tablename__ = "roles"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    name: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    workspace_members: Mapped[list["WorkspaceMember"]] = relationship(
        back_populates="role",
    )

    role_permissions: Mapped[list["RolePermission"]] = relationship(
        back_populates="role",
    )