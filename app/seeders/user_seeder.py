from sqlmodel import Session, select
from app.factories.user_factory import create_user
from app.models import User
from app.db import engine
import bcrypt

encrypted_password = bcrypt.hashpw("admin123".encode("utf-8"), bcrypt.gensalt())

initial_users = [
    {
        "username": "Etriii",
        "email": "alexarnaizaparece@gmail.com",
        "password_hash": encrypted_password,
    }
]

def seed_users(count: int = 10):
    with Session(engine) as session:
        if session.exec(select(User)).first():
            print("⚠️  Users already seeded. Skipping.")
            return

        for user_data in initial_users:
            session.add(create_user(**user_data))

        for _ in range(count):
            session.add(create_user())
        session.commit()

        print(f"✅ Seeded {count} users.")
