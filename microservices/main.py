import asyncio
import os
import boto3
from consumer import consume
from fastapi import FastAPI
from aws.services.dynamodb import DynamoDBClient

app = FastAPI()



@app.on_event('startup')
async def startup_event():
    asyncio.create_task(consume())



