FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1
RUN mkdir /django-docker-okteto
WORKDIR /django-docker-okteto
COPY . .
RUN pip install -r /requirements.txt