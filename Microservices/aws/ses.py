from aws.initialize import initialize_client_ses
import logging
import os
from dotenv import load_dotenv

load_dotenv()

def email_sender(to_addrs, subject, body_text):
    ses_client = initialize_client_ses()

    response = ses_client.send_email(
        Source=os.getenv('EMAIL_HOST_USER'),
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