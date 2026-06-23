from services.transcript_service import (
    extract_video_id,
    get_transcript
)

url = input("Enter YouTube URL: ")

print("URL RECEIVED:", repr(url))

video_id = extract_video_id(url)

print("VIDEO ID:", video_id)

transcript = get_transcript(video_id)

print(transcript[:1000])
