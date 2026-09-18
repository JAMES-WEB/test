import os
from typing import Optional

from dotenv import find_dotenv, load_dotenv
from pymongo import MongoClient

# Load the existing .env file from this folder or a parent folder.
load_dotenv(find_dotenv())

MONGODB_URI = os.getenv("MONGODB_URI") or os.getenv("MONGODB_ATLAS_CLUSTER_URI") or "mongodb://localhost:27017"
MONGODB_DATABASE = os.getenv("MONGODB_DATABASE", "community_db")

_client: Optional[MongoClient] = None
_db = None


def get_database():
    global _client, _db

    if _db is None:
        _client = MongoClient(MONGODB_URI, serverSelectionTimeoutMS=5000)
        _client.admin.command("ping")
        _db = _client[MONGODB_DATABASE]
        _db.people.create_index("email", unique=True, sparse=True)

    return _db


def close_connection():
    global _client, _db

    if _client is not None:
        _client.close()

    _client = None
    _db = None
