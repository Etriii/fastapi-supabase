from sqlmodel import create_engine, Session, SQLModel
import os
from dotenv import load_dotenv

# from sqlalchemy import text
# from sqlalchemy.inspection import inspect

load_dotenv()
DATABASE_URL = os.environ.get("DATABASE_URL")

engine = create_engine(DATABASE_URL)

# try:
#     connection = engine.connect()
#     print("Successfully connected to the database!")
#     connection.close()  # Close the connection when done
# except Exception as e:
#     print(f"Failed to connect to the database: {e}")


# try:
#     connection = engine.connect()
#     print("Successfully connected to the database!")

#     inspector = inspect(engine)
#     table_names = inspector.get_table_names()

#     if table_names:
#         print("\nTables in the database:")
#         for table_name in table_names:
#             print(f"- {table_name}")

#             try:
#                 # Fetch up to 10 rows of data from each table
#                 query = text(f"SELECT * FROM {table_name} LIMIT 10")
#                 result = connection.execute(query)
#                 rows = result.fetchall()

#                 if rows:
#                     print("  Sample Data (up to 10 rows):")
#                     columns = result.keys()
#                     print(f"    Columns: {', '.join(columns)}")
#                     for row in rows:
#                         print(f"    {row}")
#                 else:
#                     print("  No data in this table.")
#             except Exception as e:
#                 print(f"  Error fetching data from {table_name}: {e}")
#     else:
#         print("No tables found in the database.")

#     connection.close()  # Close the connection when done

# except Exception as e:
#     print(f"Failed to connect to the database: {e}")


def get_db():
    with Session(engine) as session:
        yield session


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

    
def drop_all_tables_in_db():
        SQLModel.metadata.drop_all(engine)