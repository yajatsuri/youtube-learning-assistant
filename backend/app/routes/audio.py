import os
import tempfile

from fastapi import APIRouter, UploadFile, File

from app.services.audio_service import (
    transcribe_audio
)

from app.services.video_service import (
    extract_audio
)

from app.services.llm_service import (
    generate_audio_insights
)

router = APIRouter()


VIDEO_EXTENSIONS = {
    ".mp4",
    ".mov",
    ".mkv",
    ".webm",
    ".avi"
}


@router.post("/upload-audio")
async def upload_audio(
    file: UploadFile = File(...)
):

    content = await file.read()

    if len(content) == 0:
        return {
            "error": "Uploaded file is empty"
        }

    suffix = os.path.splitext(
        file.filename
    )[1].lower()

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=suffix
    ) as temp_file:

        temp_file.write(
            content
        )

        temp_path = temp_file.name

    audio_path = None

    try:

        if suffix in VIDEO_EXTENSIONS:

            audio_path = extract_audio(
                temp_path
            )

            transcript = transcribe_audio(
                audio_path
            )

        else:

            transcript = transcribe_audio(
                temp_path
            )

        insights = generate_audio_insights(
            transcript
        )

        return {
            "filename": file.filename,
            "file_type": (
                "video"
                if suffix in VIDEO_EXTENSIONS
                else "audio"
            ),
            "transcript": transcript,
            "summary": insights["summary"],
            "key_takeaways": insights[
                "key_takeaways"
            ],
            "communication_analysis": insights[
                "communication_analysis"
            ]
        }

    finally:

        if os.path.exists(
            temp_path
        ):
            os.remove(
                temp_path
            )

        if (
            audio_path
            and os.path.exists(audio_path)
        ):
            os.remove(
                audio_path
            )
