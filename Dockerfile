# syntax=docker/dockerfile:1

FROM python:3.10-buster

WORKDIR /app

RUN pip install pipenv

COPY Pipfile .
COPY Pipfile.lock .

RUN pipenv install --system --deploy

COPY . .

ARG API_SECRET
ENV API_SECRET=${API_SECRET}
ARG DB_USER
ENV DB_USER=${DB_USER}
ARG DB_PASS
ENV DB_PASS=${DB_PASS}
ARG DB_HOST
ENV DB_HOST=${DB_HOST}
ARG DB_PORT
ENV DB_PORT=${DB_PORT}
ARG DB_NAME
ENV DB_NAME=${DB_NAME}

EXPOSE 3000

RUN pip install requests
RUN pip install Flask-HTTPAuth
RUN pip install psycopg2
RUN pip install python-dotenv
RUN pip install flask-socketio

CMD ["python3", "-m", "flask", "--app", "app/app.py", "run", "--host=0.0.0.0", "--port=3000"]
