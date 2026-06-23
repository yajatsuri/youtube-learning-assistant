from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from app.database.base import Base


class Flashcard(Base):
    __tablename__ = "flashcards"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    note_id: Mapped[int] = mapped_column(
        ForeignKey("notes.id"),
        nullable=False
    )

    question: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    answer: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    note = relationship(
        "Note",
        back_populates="flashcards"
    )
