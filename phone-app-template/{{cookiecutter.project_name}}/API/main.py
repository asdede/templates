#Example function

from fastapi import FastAPI
import httpx

app = FastAPI()

BACKEND_URL = "http://backend:5000/process"


@app.get("/call-backend")
async def call_backend():
    async with httpx.AsyncClient() as client:
        res = await client.get(BACKEND_URL)
    return {"response",res.json()}