FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install gunicorn

RUN pip install Flask

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "main:app"]
