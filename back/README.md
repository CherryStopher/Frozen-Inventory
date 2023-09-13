
To run migrations:
```
alembic upgrade head
```

To run API:

```
cd app
uvicorn main:app --reload
```