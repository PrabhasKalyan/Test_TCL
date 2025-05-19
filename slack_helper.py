from fastapi import FastAPI,Request


app = FastAPI()

@app.post("/slack/events")
async def slack_events(request:Request):
    query_params = request.query_params
    challenge = query_params.get("challenge")
    if challenge:
        return {"challenge": challenge}
    else:
        return 0    
