from fastapi import FastAPI
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound
from youtube_transcript_api.formatters import TextFormatter

app = FastAPI()

@app.get("/transcript")
async def get_transcript(video_id: str):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
        formatter = TextFormatter()
        text_transcript = formatter.format_transcript(transcript)
        return {"transcript": text_transcript}
    except (TranscriptsDisabled, NoTranscriptFound):
        return {"error": "No captions available"}
