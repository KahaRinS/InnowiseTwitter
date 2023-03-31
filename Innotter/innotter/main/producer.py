import json

import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters('rabbitmq', heartbeat=600, blocked_connection_timeout=300))
channel = connection.channel()


def publish(method, body, route):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key=route, body=json.dumps(body), properties=properties)
