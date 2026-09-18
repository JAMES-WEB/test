from datetime import datetime, timezone
from typing import Optional

from bson import ObjectId
from fastapi import APIRouter, HTTPException

from database import get_database
from schemas import PersonCreate, PersonUpdate, PersonResponse

router = APIRouter()


def serialize_person(person: dict) -> dict:
    return {
        "id": str(person["_id"]),
        "name": person["name"],
        "phone": person.get("phone"),
        "email": person.get("email"),
        "created_at": person["created_at"],
        "updated_at": person["updated_at"],
    }


def parse_id(person_id: str) -> ObjectId:
    if not ObjectId.is_valid(person_id):
        raise HTTPException(status_code=400, detail="Invalid person ID")
    return ObjectId(person_id)


@router.post("", response_model=PersonResponse, status_code=201)
def create_person(person: PersonCreate):
    collection = get_database().people
    now = datetime.now(timezone.utc)
    document = person.model_dump(exclude_none=True)
    document.update({"created_at": now, "updated_at": now})

    try:
        result = collection.insert_one(document)
    except Exception as exc:
        if "duplicate key" in str(exc).lower():
            raise HTTPException(status_code=409, detail="Email already exists")
        raise

    return serialize_person(collection.find_one({"_id": result.inserted_id}))


@router.get("", response_model=list[PersonResponse])
def list_people():
    people = get_database().people.find().sort("name", 1)
    return [serialize_person(person) for person in people]


@router.get("/{person_id}", response_model=PersonResponse)
def get_person(person_id: str):
    person = get_database().people.find_one({"_id": parse_id(person_id)})
    if not person:
        raise HTTPException(status_code=404, detail="Person not found")
    return serialize_person(person)


@router.put("/{person_id}", response_model=PersonResponse)
def update_person(person_id: str, person: PersonUpdate):
    collection = get_database().people
    object_id = parse_id(person_id)
    updates = person.model_dump(exclude_unset=True)
    updates["updated_at"] = datetime.now(timezone.utc)

    if not updates:
        raise HTTPException(status_code=400, detail="No update data provided")

    try:
        result = collection.update_one({"_id": object_id}, {"$set": updates})
    except Exception as exc:
        if "duplicate key" in str(exc).lower():
            raise HTTPException(status_code=409, detail="Email already exists")
        raise

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Person not found")

    return serialize_person(collection.find_one({"_id": object_id}))


@router.delete("/{person_id}")
def delete_person(person_id: str):
    result = get_database().people.delete_one({"_id": parse_id(person_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Person not found")
    return {"message": "Person deleted successfully"}
