import json

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.schemas.notes_schema import (
    NotesResponse,
    NoteHistoryResponse,
    NoteDetailResponse
)

from app.schemas.video_schema import (
    VideoRequest
)

from app.schemas.error_schema import (
    ErrorResponse
)

from app.services.notes_service import (
    generate_video_notes,
    get_all_notes,
    get_note_by_id
)

router = APIRouter()


@router.post(
    "/generate-notes",
    response_model=NotesResponse,
    responses={
        400: {
            "model": ErrorResponse,
            "description": "Invalid YouTube URL"
        },
        404: {
            "model": ErrorResponse,
            "description": "Transcript unavailable"
        },
        500: {
            "model": ErrorResponse,
            "description": "LLM generation failed"
        }
    }
)
def generate_notes_route(
    request: VideoRequest,
    db: Session = Depends(get_db)
):
    return generate_video_notes(
        db,
        request.youtube_url
    )


@router.get(
    "/notes",
    response_model=list[NoteHistoryResponse]
)
def get_notes_route(
    db: Session = Depends(get_db)
):
    return get_all_notes(db)


@router.get(
    "/notes/{note_id}",
    response_model=NoteDetailResponse,
    responses={
        404: {
            "model": ErrorResponse,
            "description": "Note not found"
        }
    }
)
def get_note_route(
    note_id: int,
    db: Session = Depends(get_db)
):
    note = get_note_by_id(
        db,
        note_id
    )

    if not note:
        raise HTTPException(
            status_code=404,
            detail="Note not found"
        )

    return {
        "id": note.id,
        "video_id": note.video_id,
        "video_url": note.video_url,
        "executive_summary": note.executive_summary,
        "detailed_notes": note.detailed_notes,
        "key_takeaways": json.loads(
            note.key_takeaways
        ),
        "created_at": note.created_at
    }
