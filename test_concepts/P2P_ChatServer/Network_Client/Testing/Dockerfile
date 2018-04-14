FROM python:3

RUN pip install flask

WORKDIR /app

ADD . /app

EXPOSE 8081

CMD [ "python", "NetworkClient.py" ]
