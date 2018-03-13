docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
docker build -t spicerack .
docker run -d -it -p 8080:8080 --name spicerack --network p2p spicerack
docker attach spicerack
