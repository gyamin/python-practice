from dotenv import load_dotenv
import os

load_dotenv()

user = os.getenv('DB_USER')
password = os.getenv('PASSWORD')
host = os.getenv('HOST')
port = os.getenv('PORT')
database = os.getenv('DATABASE')

URL = f'mysql://{user}:{password}@{host}:{port}/{database}'

