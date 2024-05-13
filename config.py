from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    DB_HOST=os.environ.get('DB_HOST')
    DB_USER=os.environ.get('DB_USER')
    DB_PASSWORD=os.environ.get('DB_PASSWORD')
    DB_SCHEMA=os.environ.get('DB_SCHEMA')