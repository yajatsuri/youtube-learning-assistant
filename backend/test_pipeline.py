from app.services.transcript_service import (
    extract_video_id,
    get_transcript
)

from app.services.llm_service import (
    generate_notes
)

url = "https://www.youtube.com/watch?v=rfscVS0vtbw"

video_id = extract_video_id(url)

print("Fetching transcript...")

transcript = get_transcript(video_id)

print("Generating notes...")

notes = generate_notes(transcript)

print(notes)
