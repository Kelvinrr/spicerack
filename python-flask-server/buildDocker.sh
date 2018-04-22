docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
docker build -t manager .
docker run -it -p 8080:8080 -v /path/to/spice/data:/spicedata/ -v /path/to/swagger_server/:/swaggerapp -v path/to/.ssh/:/root/.ssh/ manager
docker attach manager
