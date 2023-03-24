FROM python:3-slim-buster

WORKDIR /code/backend

COPY /requirements/requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x /code/backend/docker/*.sh

#CMD gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000
#
#EXPOSE 8000