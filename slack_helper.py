from fastapi import FastAPI,Request


app = FastAPI()

@app.post("/slack/events")
async def slack_events(request:Request):
    data = await request.json
    if data.get("type") == "url_verification":
        return {"challenge": data.get("challenge")}
    
