FROM python:3

RUN pip install flask

WORKDIR /app

ADD . /app

EXPOSE 9090

CMD [ "python", "client.py" ]
