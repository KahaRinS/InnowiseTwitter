import boto3
import botocore.config
from boto3.resources.base import ServiceResource


def initialize_db() -> ServiceResource:
    ddb = boto3.resource('dynamodb',
         endpoint_url='http://localstack:4566',
         region_name='example',
         aws_access_key_id='example',
         aws_secret_access_key='example',
         config=botocore.config.Config(signature_version=botocore.UNSIGNED))

    return ddb

def initialize_client_db() -> ServiceResource:
    ddb = boto3.client('dynamodb',
         endpoint_url='http://localstack:4566',
         region_name='example',
         aws_access_key_id='example',
         aws_secret_access_key='example',
         config=botocore.config.Config(signature_version=botocore.UNSIGNED))

    return ddb