Install this following:
```
pip install fastapi uvicorn gunicorn sqlmodel psycopg2-binary httpx

or 

pip install -r requirements.txt
```

To run migrations:

``` generate migration
alembic revision --autogenerate -m "<migration_name>"
```
In Windows:
alembic revision --autogenerate -m "Migration Message"

``` run migration
alembic upgrade head
```
In Windows:
python -m alembic upgrade head

To run seeders:

python -m app.migrate_fresh_and_seed  
note: it will reset your database data
-------------------//////-------------------

To run the app:
```
uvicorn app.main:app --reload
```
In Windows:
python -m uvicorn app.main:app --reload