FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
  xinetd p7zip-full \
  && rm -rf /var/lib/apt/lists/*

RUN pip install numpy

RUN mkdir /ctf
WORKDIR /ctf
RUN useradd -M -d /ctf ctf

RUN echo "Connection blocked" > /etc/banner_fail
COPY ctf.xinetd /etc/xinetd.d/ctf

COPY source/ /ctf/
RUN 7z x save.pkl.7z
RUN rm save.pkl.7z

RUN chown -R root:ctf /ctf && \
  chmod -R 750 /ctf

ENTRYPOINT []
CMD ["/usr/sbin/xinetd", "-dontfork"]

EXPOSE 1337
