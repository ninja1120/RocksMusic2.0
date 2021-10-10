FROM debian:latest

RUN apt update && apt upgrade -y
RUN apt-get update && apt-get upgrade -y
RUN apt-get install git curl python3-pip ffmpeg -y
RUN python3 -m pip install -U pip
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash -
RUN apt-get install -y nodejs
RUN npm install -g npm@7.24.1
RUN npm i -g npm
RUN mkdir /app/
WORKDIR /app/
COPY . /app/
RUN python3 -m pip install -U -r requirements.txt
CMD python3 main.py