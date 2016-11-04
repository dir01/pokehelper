FROM ubuntu:16.04

RUN apt-get update && apt-get install -y python-virtualenv git-core build-essential
RUN virtualenv /venv
ADD requirements.txt /tmp
RUN apt-get install -y python-dev

RUN . /venv/bin/activate && pip install -r /tmp/requirements.txt
RUN mkdir /app
ADD . /app

