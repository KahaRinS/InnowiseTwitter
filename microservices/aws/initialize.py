import boto3
import os
import botocore.config
from boto3.resources.base import ServiceResource
from dotenv import load_dotenv
from aws.credentials import AWS_KEY, AWS_REGION, AWS_ENDPOINT, AWS_SECRET_KEY

load_dotenv()

class ServiceInitialize:
    def initialize_client_db(self) -> ServiceResource:
        db = boto3.client('dynamodb',
            endpoint_url=AWS_ENDPOINT,
            region_name=AWS_REGION,
            aws_access_key_id=AWS_KEY,
            aws_secret_access_key=AWS_SECRET_KEY,
            config=botocore.config.Config(signature_version=botocore.UNSIGNED))

        return db
    def initialize_client_ses(self):
        ses_client = boto3.client(
            'ses',
            region_name=AWS_REGION,
            endpoint_url=AWS_ENDPOINT
        )
        return ses_client