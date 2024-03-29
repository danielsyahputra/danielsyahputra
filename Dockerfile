FROM python:3.9.16-slim

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get install git  -y
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT [ "bash" ]