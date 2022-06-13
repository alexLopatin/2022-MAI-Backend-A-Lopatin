FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8000
CMD [ "gunicorn", "--bind", "0.0.0.0:8000", "--workers=2", "main:app"]
