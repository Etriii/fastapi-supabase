Install this following:
```
pip install fastapi uvicorn gunicorn sqlmodel psycopg2-binary httpx
```

To run migrations:

``` generate migration
alembic revision --autogenerate -m "<migration_name>"
```
In Windows:
python -m alembic revision --autogenerate -m "<migration_name>"

``` run migration
alembic upgrade head
```
In Windows:
python -m alembic upgrade head

-------------------//////-------------------

To run the app:
```
uvicorn app.main:app --reload
```
In Windows:
python -m uvicorn app.main:app --reload