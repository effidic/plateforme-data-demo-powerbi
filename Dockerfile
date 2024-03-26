# Dockerfile
FROM python:3.9-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1

ARG TOKEN

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip --user && pip install --user -r requirements.txt

ENTRYPOINT ["python3"]

CMD ["/app/src/main.py"]