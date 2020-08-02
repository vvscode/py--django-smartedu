FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
ADD . /code

RUN pip3 install -U pipenv

RUN python3 -m pipenv install --system