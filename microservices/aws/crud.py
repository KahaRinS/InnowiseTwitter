import os
from aws.initialize import initialize_db
from dotenv import load_dotenv

load_dotenv()

def add(page_id, subscribers, posts, likes):
    table = initialize_db().Table(os.getenv('DYNAMODB_TABLE_NAME'))

    table.put_item(
        Item={
            'page_id': page_id,
            'subscribers': subscribers,
            'posts': posts,
            'likes': likes
        }
    )
def take(page_id):
    table = initialize_db().Table(os.getenv('DYNAMODB_TABLE_NAME'))
    response = table.get_item(
        Key={
            'page_id': page_id
        }
    )
    return response['Item']

def all_data():
    table = initialize_db().Table(os.getenv('DYNAMODB_TABLE_NAME'))
    response = table.scan()
    return response