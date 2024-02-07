FROM python:3.12-slim

MAINTAINER Jakub Stachowicz
LABEL authors="mikitomi21"

ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

COPY ./backend/dependencies /dependencies

RUN pip3 install -r dependencies/requirements.txt

COPY ./backend /app/backend

WORKDIR /app

RUN adduser django
RUN chown -R django /app

RUN python backend/manage.py makemigrations
RUN python backend/manage.py migrate

CMD ["python", "backend/manage.py", "runserver", "0.0.0.0:8000"]