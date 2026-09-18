from datetime import datetime, timezone

from bson import ObjectId
from pymongo.errors import DuplicateKeyError

from mongo import get_database


COLLECTION_NAME = "people"


def _collection():
    return get_database()[COLLECTION_NAME]


def _serialize(person: dict) -> dict:
    return {
        "id": str(person["_id"]),
        "name": person.get("name", ""),
        "phone": person.get("phone", ""),
        "email": person.get("email", ""),
        "created_at": person.get("created_at"),
        "updated_at": person.get("updated_at"),
    }


def create_person(name: str, phone: str = "", email: str = "") -> str:
    now = datetime.now(timezone.utc)
    document = {
        "name": name.strip(),
        "phone": phone.strip(),
        "email": email.strip() or None,
        "created_at": now,
        "updated_at": now,
    }

    try:
        result = _collection().insert_one(document)
        return str(result.inserted_id)
    except DuplicateKeyError:
        raise ValueError("This email already exists.")


def get_people() -> list[dict]:
    return [_serialize(person) for person in _collection().find().sort("name", 1)]


def get_person(person_id: str) -> dict | None:
    if not ObjectId.is_valid(person_id):
        return None

    person = _collection().find_one({"_id": ObjectId(person_id)})
    return _serialize(person) if person else None


def update_person(person_id: str, name: str, phone: str = "", email: str = "") -> bool:
    if not ObjectId.is_valid(person_id):
        return False

    updates = {
        "name": name.strip(),
        "phone": phone.strip(),
        "email": email.strip() or None,
        "updated_at": datetime.now(timezone.utc),
    }

    try:
        result = _collection().update_one(
            {"_id": ObjectId(person_id)},
            {"$set": updates},
        )
        return result.matched_count > 0
    except DuplicateKeyError:
        raise ValueError("This email already exists.")


def delete_person(person_id: str) -> bool:
    if not ObjectId.is_valid(person_id):
        return False

    result = _collection().delete_one({"_id": ObjectId(person_id)})
    return result.deleted_count > 0
