import os
import subprocess
from alembic.config import Config
from alembic import command
from sqlmodel import SQLModel
from app.db import engine
from app.seeders.user_seeder import seed_users


def drop_all_tables():
    print("Dropping all tables...")
    SQLModel.metadata.drop_all(engine)


def create_migration():
    print("Generating Alembic migration...")
    subprocess.run(
        ["alembic", "revision", "--autogenerate", "-m", "Initial Migration"], check=True
    )


def apply_migrations():
    print("Applying Alembic migrations...")
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")


def run_seeders():
    print("Running seeders...")
    seed_users()


def reset_db():
    drop_all_tables()
    create_migration()
    apply_migrations()  # if you encounter an error saying that "type "http_method_enum" already exists" just go to supabase->Enumerated Types and delete the existing one. then execeute the seeer again.


if __name__ == "__main__":
    # reset_db() #Uncomment this if you want a full reset in your db and migrations :>
    run_seeders()
    print("Database reset and seeded successfully.")
