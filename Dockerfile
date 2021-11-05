FROM python:3.9.7-slim-buster
RUN apt-get update && apt-get upgrade -y
RUN apt-get install git curl python3-pip ffmpeg -y
RUN apt-get install -y --no-install-recommends ffmpeg \
RUN apt-get clean \
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash -
RUN apt-get install -y nodejs
RUN npm install -g npm@7.24.1
COPY . /app
WORKDIR /app
RUN python3 -m pip install -U -r requirements.txt
RUN pip3 install --no-cache-dir --upgrade --requirement requirements.txt
CMD ["python3", "main.py"]