import os
import re
import logging

import requests
from dotenv import load_dotenv

from app.exceptions.custom_exceptions import (
    InvalidYoutubeUrlError,
    TranscriptUnavailableError
)

load_dotenv()

logger = logging.getLogger(__name__)

SUPADATA_API_KEY = os.getenv("SUPADATA_API_KEY")


def extract_video_id(url: str):

    logger.info("Extracting video ID from URL")

    pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11})"

    match = re.search(pattern, url)

    if not match:

        raise InvalidYoutubeUrlError(
            "Invalid YouTube URL"
        )

    return match.group(1)


def get_transcript(youtube_url: str):

    logger.info(
        "Fetching transcript from Supadata"
    )

    try:

        response = requests.get(
            "https://api.supadata.ai/v1/transcript",
            headers={
                "x-api-key": SUPADATA_API_KEY
            },
            params={
                "url": youtube_url,
                "text": "true"
            },
            timeout=60
        )

        response.raise_for_status()

        data = response.json()

        transcript = data.get("content")

        if not transcript:
            raise TranscriptUnavailableError(
                "Transcript not found."
            )

        return transcript

    except Exception as e:

        logger.exception(
            "Supadata transcript fetch failed"
        )

        raise TranscriptUnavailableError(
            str(e)
        )
