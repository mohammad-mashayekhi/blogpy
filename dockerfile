FROM python:3.12
LABEL MAINTAINER="Ma.m | raadino.com"

ENV PYTHONUNBUFFERED 1

RUN mkdir /blogpy
WORKDIR /blogpy
COPY . /blogpy

ADD requirements/requirements.txt /blogpy
RUN pip install --upgrade pip
RUN pip install requirements.txt

RUN python manage.py collectstattic --no-input

CMD ["gunicorn", "--chdir", "blogpy", "--bind", ":8000", "blog.wsgi:application"]

