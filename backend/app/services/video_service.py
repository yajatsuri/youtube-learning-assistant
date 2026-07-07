import subprocess
import tempfile


def extract_audio(video_path: str):

    output_file = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".wav"
    )

    output_path = output_file.name

    output_file.close()

    try:

        subprocess.run(
            [
                "ffmpeg",
                "-i",
                video_path,
                "-vn",
                "-acodec",
                "pcm_s16le",
                "-ar",
                "16000",
                "-ac",
                "1",
                output_path
            ],
            check=True,
            text=True,
            capture_output=True
        )

        return output_path

    except subprocess.CalledProcessError as e:

        if "does not contain any stream" in e.stderr:
            raise ValueError(
                "No audio track found in uploaded video."
            )

        raise
