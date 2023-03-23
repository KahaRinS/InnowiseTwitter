import boto3
import os
import botocore.config
from boto3.resources.base import ServiceResource
from dotenv import load_dotenv

load_dotenv()


def initialize_db() -> ServiceResource:
    ddb = boto3.resource('dynamodb',
        endpoint_url=f'{os.getenv("HOSTNAME_EXTERNAL")}:{os.getenv("PORT_EXTERNAL")}',
        region_name=os.getenv('REGION_NAME'),
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
        config=botocore.config.Config(signature_version=botocore.UNSIGNED))

    return ddb

def initialize_client_db() -> ServiceResource:
    ddb = boto3.client('dynamodb',
        endpoint_url=f'{os.getenv("HOSTNAME_EXTERNAL")}:{os.getenv("PORT_EXTERNAL")}',
        region_name=os.getenv('REGION_NAME'),
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
        config=botocore.config.Config(signature_version=botocore.UNSIGNED))

    return ddb
def initialize_client_ses():
    ses_client = boto3.client(
        'ses',
        region_name=os.getenv('REGION_NAME'),
        endpoint_url=f'{os.getenv("HOSTNAME_EXTERNAL")}:{os.getenv("PORT_EXTERNAL")}'
    )
    return ses_client