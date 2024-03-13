FROM --platform=linux/amd64 httpd as neverthoughtiwouldusehttpdforbuild

RUN apt -yq update && \
    apt -yq install nim && \
    apt -yq install binutils && \
    apt -yq install gcc

WORKDIR /tmp
COPY calc.nim .
RUN nim c -d:debug --lineDir:on --debuginfo calc.nim

FROM --platform=linux/amd64 ubuntu:latest

RUN apt -yq update && \
    apt -yq install python3 && \
    apt -yq install python3-pip

WORKDIR /app
RUN pip3 install Flask

COPY app.py /app/app.py
COPY templates /app/templates
COPY --from=neverthoughtiwouldusehttpdforbuild /tmp/calc /app/calc.elf

EXPOSE 80

ENTRYPOINT [ "python3", "app.py" ]