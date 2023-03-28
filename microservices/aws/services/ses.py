import logging

import boto3
from dotenv import load_dotenv

from aws.credentials import AWS_ENDPOINT, AWS_REGION, SES_EMAIL_HOST


load_dotenv()


class SESClient:
    """
    Class to work with SES(Simple Email Service)
    """
    def __init__(self):
        self.ses = boto3.client(
            'ses',
            region_name=AWS_REGION,
            endpoint_url=AWS_ENDPOINT
        )

    def send_email(self, to_addrs: str, subject: str, body_text: str):
        response = self.ses.send_email(
            Source=SES_EMAIL_HOST,
            Destination={'ToAddresses': to_addrs},
            Message={
                'Subject': {'Data': subject},
                'Body': {'Text': {'Data': body_text}}
            }
        )

        if response['MessageId']:
            logging.info('Email sent successfully')
        else:
            logging.error('Email sending error')


ses_client = SESClient()
