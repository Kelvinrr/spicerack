FROM python:3

RUN pip install flask pandas pyfarmhash numpy

RUN apt-get update && apt-get -y install rsync

WORKDIR /app

ADD . /app

EXPOSE 5000

EXPOSE 22

CMD [ "python", "app.py" ]
