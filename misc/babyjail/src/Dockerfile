FROM python:3.9-slim AS app

FROM pwn.red/jail
COPY --from=app / /srv
COPY challenge.py /srv/app/run
COPY txt.txt /srv/app/txt.txt
