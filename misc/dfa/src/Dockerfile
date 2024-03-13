FROM python:3.9-slim AS app


FROM pwn.red/jail
COPY --from=app / /srv
COPY txt.txt /srv/app/txt.txt
COPY chall.py /srv/app/run

