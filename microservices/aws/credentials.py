import os
from dotenv import load_dotenv

load_dotenv()

AWS_REGION = os.getenv('REGION_NAME')
AWS_ENDPOINT = f'{os.getenv("HOSTNAME_EXTERNAL")}:{os.getenv("PORT_EXTERNAL")}'
AWS_KEY = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')