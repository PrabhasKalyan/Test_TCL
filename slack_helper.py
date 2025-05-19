from fastapi import FastAPI,Request


app = FastAPI()

@app.post("/slack/events")
async def slack_events(request: Request):
    # Parse the JSON payload from the request body
    payload = await request.json()
    
    # Check if this is a URL verification request
    if "challenge" in payload:
        # Return the challenge parameter for Slack URL verification
        return {"challenge": payload["challenge"]}