import os

from dotenv import load_dotenv

load_dotenv()


class BaseConfig:
    BASE_URL: str
    DATABASE: str


class Config(BaseConfig):
    BASE_URL = 'https://jsonplaceholder.typicode.com'

    DATABASE = {
        'dbname': os.getenv('DB_NAME'),
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASS'),
        'host': os.getenv('DB_HOST'),
        'port': os.getenv('DB_PORT'),
    }


class TestConfig(BaseConfig):
    DB_CREATE = """
            CREATE DATABASE teste
            WITH
            OWNER = my_user
            ENCODING = 'UTF8'
            LC_COLLATE = 'en_US.utf8'
            LC_CTYPE = 'en_US.utf8'
            LOCALE_PROVIDER = 'libc'
            TABLESPACE = pg_default
            CONNECTION LIMIT = -1
            IS_TEMPLATE = False;
            """


class FailConfig:
    BASE_URL = 'https://jsonplaceholders.typicode.com'

    DATABASE = {
        'dbname': 'fail',
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASS'),
        'host': os.getenv('DB_HOST'),
        'port': os.getenv('DB_PORT'),
    }
