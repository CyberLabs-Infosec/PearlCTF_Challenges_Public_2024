FROM node:18-alpine3.18

RUN apk add --update nginx supervisor chromium

COPY --from=golang:1.13-alpine /usr/local/go/ /usr/local/go/
ENV PATH="/usr/local/go/bin:${PATH}" \
    CHROME_BIN="/usr/bin/chromium-browser" \
    PUPPETEER_SKIP_CHROMIUM_DOWNLOAD="true"

COPY . /home/app/
ADD supervisord.conf /etc/

WORKDIR /home/app

RUN npm i --legacy-peer-deps
RUN go build main.go

RUN cp /home/app/nginx.conf /etc/nginx/http.d/nginx.conf

WORKDIR /home/app/healthcheck
RUN go build main.go

EXPOSE 6000

ENTRYPOINT ["supervisord", "--nodaemon", "--configuration", "/etc/supervisord.conf"]