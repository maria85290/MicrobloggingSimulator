FROM python:3.9
ENV PYTHONUNBUFFERED 1

COPY app /app/app
COPY pages /app/pages
COPY static /app/static
COPY templates /app/templates
COPY tweets /app/tweets
COPY manage.py /app
COPY requirements.txt /app

RUN pip install -r /app/requirements.txt


WORKDIR /app