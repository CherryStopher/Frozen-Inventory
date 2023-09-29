
Python 3.10.x

To run migrations:
```
cd back
alembic upgrade head
```

To run API:

```
cd back/app
uvicorn main:app --reload
```