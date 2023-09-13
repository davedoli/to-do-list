FROM python:3.11.4-slim-buster
#set workdir to todo
WORKDIR /usr/src/to_do
#set a build-time arguement for 
ARG YOUR_ENV
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#install packages
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

#copy all the files in to_do parent folder
COPY . /