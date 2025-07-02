from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import StreamingResponse
import httpx
import asyncio

app = FastAPI()

OLLAMA_HOST = "http://localhost:11434"

@app.get("/")
async def root():
    return {"message": "Proxy is running"}

@app.get("/api/tags")
async def get_tags():
    async with httpx.AsyncClient() as client:
        try:
            r = await client.get(f"{OLLAMA_HOST}/api/tags")
            r.raise_for_status()
            return r.json()
        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=e.response.status_code, detail=str(e))

@app.post("/api/chat")
async def chat_proxy(request: Request):
    data = await request.json()
    data["think"] = False  # ensure think is always false

    async def event_generator():
        async with httpx.AsyncClient(timeout=None) as client:
            async with client.stream("POST", f"{OLLAMA_HOST}/api/chat", json=data) as response:
                response.raise_for_status()
                async for chunk in response.aiter_bytes():
                    yield chunk

    return StreamingResponse(event_generator(), media_type="application/json")
