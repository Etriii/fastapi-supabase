from sqlmodel import create_engine, Session, SQLModel

# Replace with your actual database URL
DATABASE_URL = "postgresql://postgres:utotsabao123@db.crisvqjlydstegwtgnlz.supabase.co:5432/postgres"

engine = create_engine(DATABASE_URL)

def get_db():
    with Session(engine) as session:
        yield session

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)