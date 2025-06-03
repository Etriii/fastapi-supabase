from sqlmodel import Session
from app.factories.user_factory import create_user
from app.models import User
from app.db import engine


def seed_users(count: int = 10):
    with Session(engine) as session:
        if session.exec(User.select()).first():
            print("⚠️  Users already seeded. Skipping.")
            return

        for _ in range(count):
            session.add(create_user())
        session.commit()

        print(f"✅ Seeded {count} users.")
