from datetime import datetime

from sqlalchemy import String, Text, DateTime
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)
from app.database.base import Base


class Note(Base):
    __tablename__ = "notes"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    video_id: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    video_url: Mapped[str] = mapped_column(
        String(500),
        nullable=False
    )

    title: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True
    )

    executive_summary: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    detailed_notes: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    key_takeaways: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )
