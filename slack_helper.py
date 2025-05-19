from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, Dict

app = FastAPI()

# Define the structure of the Slack payload
class SlackEvent(BaseModel):
    type: Optional[str]
    challenge: Optional[str]
    event: Optional[Dict]

@app.post("/slack/events")
def slack_events(payload: SlackEvent):  # FastAPI automatically parses JSON into `payload`
    if payload.type == "url_verification":
        return {"challenge": payload.challenge}
    else:
        return {"ok": True}
