from fastapi import Request
from fastapi.responses import JSONResponse

from app.exceptions.custom_exceptions import (
    InvalidYoutubeUrlError,
    TranscriptUnavailableError,
    LLMGenerationError
)


def register_exception_handlers(app):

    @app.exception_handler(
        InvalidYoutubeUrlError
    )
    async def invalid_url_handler(
        request: Request,
        exc: InvalidYoutubeUrlError
    ):
        return JSONResponse(
            status_code=400,
            content={
                "error": str(exc)
            }
        )

    @app.exception_handler(
        TranscriptUnavailableError
    )
    async def transcript_handler(
        request: Request,
        exc: TranscriptUnavailableError
    ):
        return JSONResponse(
            status_code=404,
            content={
                "error": str(exc)
            }
        )

    @app.exception_handler(
        LLMGenerationError
    )
    async def llm_handler(
        request: Request,
        exc: LLMGenerationError
    ):
        return JSONResponse(
            status_code=500,
            content={
                "error": str(exc)
            }
        )
