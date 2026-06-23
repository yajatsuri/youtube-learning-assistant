import re
import logging

from youtube_transcript_api import (
    YouTubeTranscriptApi
)

from app.exceptions.custom_exceptions import (
    InvalidYoutubeUrlError,
    TranscriptUnavailableError
)

logger = logging.getLogger(__name__)


def extract_video_id(url: str):

    logger.info(
        "Extracting video ID from URL"
    )

    pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11})"

    match = re.search(
        pattern,
        url
    )

    if not match:

        logger.warning(
            f"Invalid YouTube URL received: {url}"
        )

        raise InvalidYoutubeUrlError(
            "Invalid YouTube URL"
        )

    video_id = match.group(1)

    logger.info(
        f"Video ID extracted successfully: {video_id}"
    )

    return video_id


def get_transcript(video_id: str):

    logger.info(
        f"Fetching transcript for video: {video_id}"
    )

    try:

        api = YouTubeTranscriptApi()

        transcript = api.fetch(
            video_id
        )

        transcript_text = " ".join(
            snippet.text
            for snippet in transcript
        )

        logger.info(
            "Transcript fetched successfully"
        )

        return transcript_text

    except Exception:

        logger.exception(
            f"Transcript fetch failed for video: {video_id}"
        )

        raise TranscriptUnavailableError(
            f"Transcript unavailable for video: {video_id}"
        )
