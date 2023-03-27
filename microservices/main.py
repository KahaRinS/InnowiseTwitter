import asyncio
from fastapi import FastAPI
from consumer import consume


app = FastAPI()


@app.on_event('startup')
async def startup_event():
    asyncio.create_task(consume())
