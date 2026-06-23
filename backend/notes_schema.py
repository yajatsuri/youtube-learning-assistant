kfrom datetime import datetime

from pydantic import BaseModel


class NotesResponse(BaseModel):
    executive_summary: str
    detailed_notes: str
    key_takeaways: list[str]


class NoteHistoryResponse(BaseModel):
    id: int
    video_id: str
    video_url: str
    created_at: datetime

    class Config:
        from_attributes = True


class NoteDetailResponse(BaseModel):
    id: int
    video_id: str
    video_url: str
    executive_summary: str
    detailed_notes: str
    key_takeaways: list[str]
    created_at: datetime
