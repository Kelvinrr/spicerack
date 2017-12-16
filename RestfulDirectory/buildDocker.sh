docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
docker build -t manager .
docker run -i -p 5000:5000 manager
