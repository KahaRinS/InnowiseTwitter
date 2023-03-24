import os
from aws.initialize import ServiceInitialize
from dotenv import load_dotenv

load_dotenv()


class DynamoCrud:
    db = ServiceInitialize().initialize_client_db()
    def add(self, page_id, subscribers, posts, likes):

        self.db.put_item(
            TableName=os.getenv('DYNAMODB_TABLE_NAME'),
            Item={
                'page_id': {'S': page_id},
                'subscribers': {'N': subscribers},
                'posts': {'N': posts},
                'likes': {'N': likes}
            }
        )
    def take(self, page_id):
        response = self.db.get_item(
            TableName=os.getenv('DYNAMODB_TABLE_NAME'),
            Key={
                'page_id': {'S': page_id},
            }
        )
        return response['Item']

    def all_data(self):
        response = self.db.scan(
            TableName=os.getenv('DYNAMODB_TABLE_NAME'),
        )
        return response['Items']
