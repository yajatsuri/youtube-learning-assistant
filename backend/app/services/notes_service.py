import json

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.note import Note

from app.services.transcript_service import (
    extract_video_id,
    get_transcript
)

from app.services.llm_service import (
    generate_notes
)


def generate_video_notes(
    db: Session,
    youtube_url: str
):
    """
    Main business workflow.

    URL
      ↓
    Video ID
      ↓
    Transcript
      ↓
    LLM Notes
      ↓
    Save To PostgreSQL
      ↓
    Return Structured Notes
    """

    video_id = extract_video_id(
        youtube_url
    )

    transcript = get_transcript(
       youtube_url
    )

    notes = generate_notes(
        transcript
    )

    note = Note(
        video_id=video_id,
        video_url=youtube_url,
        title=None,
        executive_summary=notes[
            "executive_summary"
        ],
        detailed_notes=notes[
            "detailed_notes"
        ],
        key_takeaways=json.dumps(
            notes["key_takeaways"]
        )
    )

    db.add(note)

    db.commit()

    db.refresh(note)

    return notes


def get_all_notes(
    db: Session
):
    stmt = (
        select(Note)
        .order_by(
            Note.created_at.desc()
        )
    )

    result = db.execute(
        stmt
    )

    return result.scalars().all()


def get_note_by_id(
    db: Session,
    note_id: int
):
    return db.get(
        Note,
        note_id
    )
