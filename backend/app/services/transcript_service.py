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

    except Exception as e:

        logger.exception(
            f"Transcript fetch failed for video: {video_id}"
        )

        raise TranscriptUnavailableError(
            str(e)
        )
