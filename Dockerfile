FROM tiangolo/uwsgi-nginx-flask:python3.6

RUN mkdir -p /usr/src/app
RUN rm -r /app
WORKDIR /usr/src/app
COPY . /usr/src/app

RUN apt-get update
RUN apt-get install -y --reinstall ca-certificates
RUN pip3 install --no-cache-dir -r /usr/src/app/requirements.txt
RUN export REQUESTS_CA_BUNDLE=/etc/ssl/certs

ENV UWSGI_INI /usr/src/app/uwsgi.ini
ENV LISTEN_PORT 8080

EXPOSE 8080

