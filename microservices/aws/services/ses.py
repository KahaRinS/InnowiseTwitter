import logging
import os
import boto3
from dotenv import load_dotenv
from aws.credentials import AWS_REGION, AWS_ENDPOINT, SES_EMAIL_HOST

load_dotenv()

class SESClient:
    def __init__(self):
        self.ses = boto3.client(
            'ses',
            region_name=AWS_REGION,
            endpoint_url=AWS_ENDPOINT
        )

    def email_sender(self, to_addrs, subject, body_text):
        response = self.ses.send_email(
            Source=SES_EMAIL_HOST,
            Destination={'ToAddresses': to_addrs},
            Message={
                'Subject': {'Data': subject},
                'Body': {'Text': {'Data': body_text}}
            }
        )

        if response['MessageId']:
            logging.info('Письмо отправлено успешно')
        else:
            logging.error('Ошибка отправки письма')