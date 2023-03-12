import boto3
from DynamoDB.db import initialize_client_db, initialize_db

db = initialize_db()
ddb = initialize_client_db()


def generate_table():
    response = ddb.list_tables()

    if not 'Pages' in response['TableNames']:
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
        print('Successfully created table Recipes')
    else:
        print('Table already exists')