from ..models import User
from faker import Faker
from datetime import datetime
import bcrypt

faker = Faker()


def create_user(username=None, email=None, password_hash=None) -> User:
    return User(
        username=username or faker.user_name(),
        email=email or faker.email(),
        password_hash=password_hash
        or bcrypt.hashpw("admin123".encode("utf-8"), bcrypt.gensalt()),
        created_at=datetime.now(),
    )
