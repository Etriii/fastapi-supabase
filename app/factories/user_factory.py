from ..models import User
from faker import Faker
from datetime import datetime

faker = Faker()


def create_user(username=None) -> User:
    return User(
        username=username or faker.user_name(),
        email=faker.email(),
        password_hash="hashed-password",
        created_at=datetime.now(),
    )
