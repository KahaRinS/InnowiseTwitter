import ast
import asyncio
import logging
import os

import aio_pika
from dotenv import load_dotenv

from aws.services.dynamodb import db_client

load_dotenv()


async def message_handler(message: aio_pika.IncomingMessage):
    async with message.process():
        mydata = ast.literal_eval(message.body.decode("UTF-8"))
        db_client.add_page(page_id=mydata['page_id'],
                           subscribers=mydata['subscribers'],
                           posts=mydata['posts'], likes=mydata['likes'])


async def consume():
    connection = await aio_pika.connect_robust(
        os.getenv('BROCKER_URL'),
        loop=asyncio.get_running_loop()
    )
    channel = await connection.channel()
    queue_name = os.getenv('RABBIT_QUEUE')
    queue = await channel.declare_queue(queue_name, durable=True)

    await queue.consume(message_handler)

    logging.info(f' [*] Waiting for messages on {queue_name}. To exit press CTRL+C')
