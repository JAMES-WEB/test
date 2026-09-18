import os
from typing import Optional

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

_client: Optional[MongoClient] = None
database = None


def connect_to_database():
    global _client, database

    uri = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
    database_name = os.getenv("MONGODB_DATABASE", "community_db")

    _client = MongoClient(uri, serverSelectionTimeoutMS=5000)
    _client.admin.command("ping")
    database = _client[database_name]
    database.people.create_index("email", unique=True, sparse=True)


def get_database():
    if database is None:
        connect_to_database()
    return database


def close_database_connection():
    global _client, database
    if _client is not None:
        _client.close()
    _client = None
    database = None
