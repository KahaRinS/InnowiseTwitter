import logging
import boto3
import os
import botocore.config
from boto3.resources.base import ServiceResource
from aws.credentials import AWS_KEY, AWS_REGION, AWS_ENDPOINT, AWS_SECRET_KEY, DYNAMODB_TABLE

class DynamoDBClient():

    def __init__(self):
        self.db = boto3.client('dynamodb',
            endpoint_url=AWS_ENDPOINT,
            region_name=AWS_REGION,
            aws_access_key_id=AWS_KEY,
            aws_secret_access_key=AWS_SECRET_KEY,
            config=botocore.config.Config(signature_version=botocore.UNSIGNED)
        )

    def generate_table(self):
        response = self.db.list_tables()
        if DYNAMODB_TABLE not in response['TableNames']:
            self.db.create_table(
                TableName='Pages',
                KeySchema=[
                    {
                        'AttributeName': 'page_id',
                        'KeyType': 'HASH'  # Partition key
                    }
                ],
                AttributeDefinitions=[
                    {
                        'AttributeName': 'page_id',
                        'AttributeType': 'S'  # String
                    }
                ],
                ProvisionedThroughput={
                    'ReadCapacityUnits': 5,
                    'WriteCapacityUnits': 5
                }
            )
            logging.info('Successfully created table Recipes')
        else:
            logging.info('Table already exists')

    def add(self, page_id, subscribers, posts, likes):

        self.db.put_item(
            TableName=DYNAMODB_TABLE,
            Item={
                'page_id': {'S': page_id},
                'subscribers': {'N': subscribers},
                'posts': {'N': posts},
                'likes': {'N': likes}
            }
        )
    def take(self, page_id):
        response = self.db.get_item(
            TableName=DYNAMODB_TABLE,
            Key={
                'page_id': {'S': page_id},
            }
        )
        return response['Item']

    def all_data(self):
        response = self.db.scan(
            TableName=DYNAMODB_TABLE,
        )
        return response['Items']