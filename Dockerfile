FROM python:3.9.2

LABEL MAINTAINER="Clement Maciejewski"
LABEL DESCRIPTION="Simple Flask App respecting Dockerfile best practices"

COPY app app
WORKDIR /app

ENV FLASK_APP="app.py"

RUN pip3 install \
    flask

ENTRYPOINT flask run --host="0.0.0.0"