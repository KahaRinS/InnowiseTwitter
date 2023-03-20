import asyncio
import os

from consumer import consume
from DynamoDB.db import initialize_client_db, initialize_db
from fastapi import FastAPI

app = FastAPI()

db = initialize_db()
ddb = initialize_client_db()


@app.on_event('startup')
async def startup_event():
    asyncio.create_task(consume())

@app.get('/')
def index():
    return 'Hello World'

