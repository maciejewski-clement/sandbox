FROM python:3.9.2

LABEL MAINTAINER="Clement Maciejewski"
LABEL DESCRIPTION="Flask image with uWSGI"
LABEL NAME="flask-sandbox"

COPY app app
WORKDIR /app

ENV FLASK_APP="app.py"

RUN pip3 install \
        flask \
        uwsgi

ENTRYPOINT uwsgi --ini uwsgi.ini