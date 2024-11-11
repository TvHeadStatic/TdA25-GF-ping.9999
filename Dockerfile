# syntax=docker/dockerfile:1

FROM python:3.10-buster

WORKDIR /

RUN pip install pipenv

COPY . .

EXPOSE 80

CMD ["/start.sh"]