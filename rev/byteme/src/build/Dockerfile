FROM --platform=linux/amd64 python:3.13.0a4

COPY byteme.py /app/byteme.py

WORKDIR /app
RUN python -m compileall byteme.py

CMD [ "sleep", "infinity" ]
