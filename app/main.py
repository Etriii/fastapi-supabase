from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from app.db import create_db_and_tables, drop_all_tables_in_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Connecting to DB...")    
    try:
        drop_all_tables_in_db()
        create_db_and_tables()
        print("Tables created.")
    except Exception as e:
        print(f"Failed to create DB tables: {e}")

    yield  

    print("Disconnecting from DB...")

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)
