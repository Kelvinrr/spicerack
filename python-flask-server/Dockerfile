# For an example on how to run this docker container, 
# please check the buildDocker.sh script... or just configure and run the script!

FROM python:3-alpine

RUN echo "http://dl-8.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories
RUN apk --no-cache --update-cache add gcc gfortran python3 python-dev py-pip build-base wget freetype-dev libpng-dev openblas-dev
RUN apk add rsync openssh
RUN ln -s /usr/include/locale.h /usr/include/xlocale.h
RUN mkdir -p /usr/src/app
RUN mkdir -p /root/.ssh

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /usr/src/app/

COPY . /spicedata/

COPY . /swaggerapp/

ADD . /root/.ssh/

RUN chmod 700 /root/.ssh

EXPOSE 8080

ENTRYPOINT ["python3"]

CMD ["-m", "swagger_server"]
