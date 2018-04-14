docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
docker build -t spice .
docker run -d -it -p 9090:9090 --name spice --network p2p spice
docker attach spice
