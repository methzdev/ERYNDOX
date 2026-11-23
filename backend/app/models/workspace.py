import uuid
from typing import TYPE_CHECKING

from sqlalchemy import String, CheckConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

if TYPE_CHECKING:
    from app.models.workspace_member import WorkspaceMember


class Workspace(Base):
    __tablename__ = "workspaces"

    __table_args__ = (
        CheckConstraint(
            "workspace_type IN ('personal', 'organization')",
            name="ck_workspaces_workspace_type",
        ),
    )

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    name: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    workspace_type: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    members: Mapped[list["WorkspaceMember"]] = relationship(
        back_populates="workspace",
    )