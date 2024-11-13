# syntax=docker/dockerfile:1

FROM python:3.10-buster

WORKDIR /app

RUN pip install pipenv

COPY Pipfile .
COPY Pipfile.lock .

RUN pipenv install --system --deploy

COPY . .

ENV FOO=${FOO}

EXPOSE 3000

CMD ["python3", "-m", "flask", "--app", "app/app.py", "run", "--host=0.0.0.0", "--port=3000"]
