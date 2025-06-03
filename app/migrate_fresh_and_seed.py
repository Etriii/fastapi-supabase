from alembic.config import Config
from alembic import command
from app.seeders.user_seeder import seed_users

# import other seeders here


def reset_database():
    alembic_cfg = Config("alembic.ini")
    command.downgrade(alembic_cfg, "base")
    command.upgrade(alembic_cfg, "head")


def run_seeders():
    seed_users()

if __name__ == "__main__":
    reset_database()
    run_seeders()
