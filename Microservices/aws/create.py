import boto3
from aws.initialize import initialize_client_db, initialize_db
import logging

db = initialize_db()
ddb = initialize_client_db()


def generate_table():
    response = ddb.list_tables()

    if 'Pages' not in response['TableNames']:
        db.create_table(
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