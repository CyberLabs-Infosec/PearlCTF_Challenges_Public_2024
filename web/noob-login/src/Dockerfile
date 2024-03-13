FROM python:3-alpine

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 9000
CMD ["gunicorn","--config", "gunicorn_config.py", "app:app"]
