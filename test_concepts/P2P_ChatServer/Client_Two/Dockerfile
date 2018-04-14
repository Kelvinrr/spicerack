FROM python:3

RUN pip install flask

WORKDIR /app

ADD . /app

EXPOSE 8080

CMD [ "python", "client.py" ]
