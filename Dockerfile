FROM ubuntu:20.04

RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get install -y python3-pip

COPY ./src/requirements.txt /scripts/

RUN pip3 install -r /scripts/requirements.txt

RUN pip3 install celery
RUN mkdir /src
WORKDIR /src

