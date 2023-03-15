FROM python:3-slim-buster

RUN mkdir /code

WORKDIR /code

COPY /requirements/requirements.txt .

RUN pip install -r requirements.txt

COPY . .

WORKDIR src

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]

EXPOSE 8000