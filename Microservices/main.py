import asyncio
import os
import boto3
from aws.crud import all_data
from consumer import consume
from aws.initialize import initialize_client_db, initialize_db, initialize_client_ses
from fastapi import FastAPI

app = FastAPI()

db = initialize_db()
ddb = initialize_client_db()


@app.on_event('startup')
async def startup_event():
    asyncio.create_task(consume())


