FROM python:3.7-rc-stretch

RUN pip install flask
RUN mkdir -p /opt/app

COPY . /opt/app/

CMD python /opt/app/app.py