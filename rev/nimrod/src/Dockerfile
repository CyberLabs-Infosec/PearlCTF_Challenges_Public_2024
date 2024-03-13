FROM --platform=linux/amd64 ubuntu:latest

RUN apt -yq update && \
    apt -yq install tcpdump && \
    apt -yq install curl

RUN useradd -d /home/n00b -s /bin/bash n00b

COPY admin /home/n00b/admin
COPY next_amazon /home/n00b/next_amazon
RUN chown -R n00b:n00b /home/n00b

CMD /bin/sh; sleep infinity
