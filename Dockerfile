FROM python:3

RUN pip install flask

WORKDIR /app

ADD . /app

EXPOSE 5000

CMD [ "python", "app.py" ]
