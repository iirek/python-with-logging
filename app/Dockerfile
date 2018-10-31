FROM python:3.7-rc-stretch

RUN apt-get update && apt-get install -y  libpq-dev libev-dev

RUN pip install flask
RUN pip install bjoern
RUN mkdir -p /opt/app

COPY . /opt/app/
WORKDIR /opt/app

CMD python app_server.py