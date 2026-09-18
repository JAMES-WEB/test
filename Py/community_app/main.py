from contextlib import asynccontextmanager

from fastapi import FastAPI

from database import close_database_connection, connect_to_database
from crud import router as people_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    connect_to_database()
    yield
    close_database_connection()


app = FastAPI(
    title="Community App API",
    version="1.0.0",
    lifespan=lifespan,
)

app.include_router(people_router, prefix="/people", tags=["People"])


@app.get("/")
def root():
    return {"message": "Community App API is running"}
