FROM python:3.9-slim-buster

RUN apt-get update

RUN apt-get install libpq-dev gcc -y
RUN pip install flask
RUN pip install flask-cors

RUN pip install flask-marshmallow

RUN pip install flask-sqlalchemy

RUN pip install psycopg2
WORKDIR /app

COPY . /app

EXPOSE 5000

CMD ["python3", "public_demo.py"]







