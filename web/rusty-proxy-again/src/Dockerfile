FROM rust:alpine3.18
RUN apk add --no-cache --update npm supervisor

COPY ./ /home/chall/

WORKDIR /home/chall/http_proxy
RUN cargo build

WORKDIR /home/chall/app/api
RUN npm install --legacy-peer-deps

ADD supervisord.conf /etc/

ENTRYPOINT ["supervisord", "--nodaemon", "--configuration", "/etc/supervisord.conf"]