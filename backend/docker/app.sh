#!/bin/bash

cd alembic_fake

alembic upgrade head

cd ..

alembic upgrade head

cd src

gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000
