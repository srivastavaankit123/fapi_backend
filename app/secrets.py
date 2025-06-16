import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.environ.get('DATABASE_URL')
AUTHJWT_SECRET_KEY = os.environ.get('AUTHJWT_SECRET_KEY')