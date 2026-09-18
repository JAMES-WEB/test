from contextlib import asynccontextmanager
from datetime import datetime
from typing import List
import os

from bson.objectid import ObjectId
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, EmailStr, Field

from mongo_database import DatabaseManager


# ---------------------------------------------------------
# LOAD ENVIRONMENT VARIABLES
# ---------------------------------------------------------

load_dotenv()

mongo_url = os.getenv('MONGODB_ATLAS_CLUSTER_URI')

# ---------------------------------------------------------
# DATABASE
# ---------------------------------------------------------

try:
    db = DatabaseManager()
except Exception as e:
    print(f"Failed to connect to MongoDB: {e}")
    db = None


# ---------------------------------------------------------
# FASTAPI LIFESPAN
# ---------------------------------------------------------

@asynccontextmanager
async def lifespan(app: FastAPI):

    if db is None:
        raise RuntimeError(
            "Failed to connect to MongoDB."
        )

    yield

    if db:
        db.close_connection()


# ---------------------------------------------------------
# FASTAPI APP
# ---------------------------------------------------------

app = FastAPI(
    title="MongoDB Database API",
    version="1.0.0",
    lifespan=lifespan
)


# ---------------------------------------------------------
# PYDANTIC MODELS
# ---------------------------------------------------------

class UserCreate(BaseModel):
    name: str = Field(min_length=1)
    email: EmailStr
    age: int = Field(ge=1, le=120)


class UserResponse(BaseModel):
    id: str
    name: str
    email: str
    age: int
    created_at: datetime


class PostCreate(BaseModel):
    user_id: str
    title: str = Field(min_length=1)
    content: str = Field(min_length=1)


class PostResponse(BaseModel):
    id: str
    user_id: str
    title: str
    content: str
    created_at: datetime


class PostUpdate(BaseModel):
    title: str = Field(min_length=1)
    content: str = Field(min_length=1)


# ---------------------------------------------------------
# ROOT
# ---------------------------------------------------------

@app.get("/")
async def root():

    return {
        "message": "MongoDB Database API",
        "version": "1.0.0",
        "status": "running"
    }


# =========================================================
# USER API
# =========================================================

# ---------------------------------------------------------
# CREATE USER
# ---------------------------------------------------------

@app.post(
    "/users/",
    response_model=dict,
    status_code=status.HTTP_201_CREATED
)
async def create_user(user: UserCreate):

    try:

        user_id = db.create_user(
            user.name,
            str(user.email),
            user.age
        )

        if not user_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User could not be created. The email may already exist."
            )

        return {
            "message": "User created successfully",
            "user_id": user_id
        }

    except HTTPException:
        raise

    except Exception as e:

        print(
            "[FASTAPI ERROR]",
            type(e).__name__,
            repr(e)
        )

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"MongoDB error: {str(e)}"
        )

# ---------------------------------------------------------
# GET ALL USERS
# ---------------------------------------------------------

@app.get(
    "/users/",
    response_model=List[UserResponse]
)
async def get_all_users():

    try:

        users = db.get_all_users()

        return [
            UserResponse(
                id=str(user["_id"]),
                name=user["name"],
                email=user["email"],
                age=user["age"],
                created_at=user["created_at"]
            )
            for user in users
        ]

    except Exception as e:

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal server error: {str(e)}"
        )


# ---------------------------------------------------------
# GET ONE USER
# ---------------------------------------------------------

@app.get(
    "/users/{user_id}",
    response_model=UserResponse
)
async def get_user(user_id: str):

    try:

        if not ObjectId.is_valid(user_id):

            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid user ID format"
            )

        user = db.get_user(user_id)

        if not user:

            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        return UserResponse(
            id=str(user["_id"]),
            name=user["name"],
            email=user["email"],
            age=user["age"],
            created_at=user["created_at"]
        )

    except HTTPException:
        raise

    except Exception as e:

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal server error: {str(e)}"
        )


# ---------------------------------------------------------
# UPDATE USER
# ---------------------------------------------------------

@app.put(
    "/users/{user_id}",
    response_model=dict
)
async def update_user(
    user_id: str,
    user_update: UserCreate
):

    try:

        if not ObjectId.is_valid(user_id):

            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid user ID format"
            )

        existing_user = db.get_user(user_id)

        if not existing_user:

            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        success = db.update_user(
            user_id,
            user_update.name,
            str(user_update.email),
            user_update.age
        )

        if not success:

            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Update failed. Email might already exist."
            )

        return {
            "message": "User updated successfully"
        }

    except HTTPException:
        raise

    except Exception as e:

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal server error: {str(e)}"
        )


# ---------------------------------------------------------
# DELETE USER
# ---------------------------------------------------------

@app.delete(
    "/users/{user_id}",
    response_model=dict
)
async def delete_user(user_id: str):

    try:

        if not ObjectId.is_valid(user_id):

            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid user ID format"
            )

        user = db.get_user(user_id)

        if not user:

            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        success = db.delete_user(user_id)

        if not success:

            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Failed to delete user"
            )

        return {
            "message": "User and associated posts deleted successfully"
        }

    except HTTPException:
        raise

    except Exception as e:

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal server error: {str(e)}"
        )


# =========================================================
# POST API
# =========================================================

# ---------------------------------------------------------
# CREATE POST
# ---------------------------------------------------------

@app.post(
    "/posts/",
    response_model=dict,
    status_code=status.HTTP_201_CREATED
)
async def create_post(post: PostCreate):

    try:

        if not ObjectId.is_valid(post.user_id):

            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid user ID format"
            )

        user = db.get_user(post.user_id)

        if not user:

            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        post_id = db.create_post(
            post.user_id,
            post.title,
            post.content
        )

        if not post_id:

            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Failed to create post"
            )

        return {
            "message": "Post created successfully",
            "post_id": post_id
        }

    except HTTPException:
        raise

    except Exception as e:

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal server error: {str(e)}"
        )


# ---------------------------------------------------------
# GET ALL POSTS
# ---------------------------------------------------------

@app.get(
    "/posts/",
    response_model=List[PostResponse]
)
async def get_all_posts():

    try:

        posts = db.get_all_posts()

        return [
            PostResponse(
                id=str(post["_id"]),
                user_id=str(post["user_id"]),
                title=post["title"],
                content=post["content"],
                created_at=post["created_at"]
            )
            for post in posts
        ]

    except Exception as e:

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal server error: {str(e)}"
        )


# ---------------------------------------------------------
# GET POSTS BY USER
# ---------------------------------------------------------

@app.get(
    "/users/{user_id}/posts",
    response_model=List[PostResponse]
)
async def get_user_posts(user_id: str):

    try:

        if not ObjectId.is_valid(user_id):

            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid user ID format"
            )

        user = db.get_user(user_id)

        if not user:

            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        posts = db.get_user_posts(user_id)

        return [
            PostResponse(
                id=str(post["_id"]),
                user_id=str(post["user_id"]),
                title=post["title"],
                content=post["content"],
                created_at=post["created_at"]
            )
            for post in posts
        ]

    except HTTPException:
        raise

    except Exception as e:

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal server error: {str(e)}"
        )


# ---------------------------------------------------------
# UPDATE POST
# ---------------------------------------------------------

@app.put(
    "/posts/{post_id}",
    response_model=dict
)
async def update_post(
    post_id: str,
    post_update: PostUpdate
):

    try:

        if not ObjectId.is_valid(post_id):

            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid post ID format"
            )

        existing_post = db.get_post(post_id)

        if not existing_post:

            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Post not found"
            )

        success = db.update_post(
            post_id,
            post_update.title,
            post_update.content
        )

        if not success:

            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Failed to update post"
            )

        return {
            "message": "Post updated successfully"
        }

    except HTTPException:
        raise

    except Exception as e:

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal server error: {str(e)}"
        )


# ---------------------------------------------------------
# DELETE POST
# ---------------------------------------------------------

@app.delete(
    "/posts/{post_id}",
    response_model=dict
)
async def delete_post(post_id: str):

    try:

        if not ObjectId.is_valid(post_id):

            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid post ID format"
            )

        existing_post = db.get_post(post_id)

        if not existing_post:

            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Post not found"
            )

        success = db.delete_post(post_id)

        if not success:

            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Failed to delete post"
            )

        return {
            "message": "Post deleted successfully"
        }

    except HTTPException:
        raise

    except Exception as e:

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal server error: {str(e)}"
        )


# ---------------------------------------------------------
# RUN DIRECTLY
# ---------------------------------------------------------

if __name__ == "__main__":

    import uvicorn

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8001
    )