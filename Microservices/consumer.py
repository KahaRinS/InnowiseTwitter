import ast
import asyncio
import os
import logging

import aio_pika
from DynamoDB.crud import add


async def message_handler(message: aio_pika.IncomingMessage):
    async with message.process():
        mydata = ast.literal_eval(message.body.decode("UTF-8"))
        add(mydata['page_id'], mydata['subscribers'], mydata['posts'], mydata['likes'])


async def consume():
    connection = await aio_pika.connect_robust(
        'amqp://guest:guest@rabbitmq/',
        loop=asyncio.get_running_loop()
    )

    channel = await connection.channel()
    queue_name = os.environ.get('RABBIT_QUEUE')
    queue = await channel.declare_queue(queue_name, durable=True)

    await queue.consume(message_handler)

    logging.info(f' [*] Waiting for messages on {queue_name}. To exit press CTRL+C')

