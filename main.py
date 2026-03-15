from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from youtube_transcript_api import YouTubeTranscriptApi

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/transcript/{video_id}")
def get_transcript(video_id: str):
    try:
        ytt = YouTubeTranscriptApi()
        transcript = ytt.fetch(video_id)
        full_text = " ".join([t.text for t in transcript])
        return {"success": True, "transcript": full_text}
    except Exception as e:
        return {"success": False, "error": str(e)}
