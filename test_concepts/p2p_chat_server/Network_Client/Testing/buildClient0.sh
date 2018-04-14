docker build -t spice .
docker run -d -it -p 8081:8081 --name spice --network p2p spice
docker attach spice
