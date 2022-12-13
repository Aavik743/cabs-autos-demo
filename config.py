import os
from pathlib import Path
from dotenv import load_dotenv


env_path = Path('.') / '.env'
load_dotenv(verbose=True, dotenv_path=env_path)

from mongoengine import connect

DEFAULT_CONNECTION_NAME = connect(os.getenv('MONGODB_DB'))


MONGO_DB = {
    # 'MONGODB_DB': os.getenv('MONGODB_DB', 'cabs_autos_db'),
    'MONGODB_HOST': os.getenv('MONGODB_HOST', 'localhost'),
    'MONGODB_PORT': int(os.getenv('MONGODB_PORT', 27017)),
    'MONGODB_USERNAME': os.getenv('MONGODB_USERNAME', ''),
    'MONGODB_PASSWORD': os.getenv('MONGODB_PASSWORD', ''),
}

if os.getenv('MONGODB_DB_URL') is not None and len(os.getenv('MONGODB_DB_URL')) != 0:
    MONGO_DB['MONGODB_SETTINGS'] = {
        'host': os.getenv('MONGODB_DB_URL')  # example: 'mongodb://username:password@localhost/test'
    }

PORT = os.getenv('FLASK_RUN_PORT')
