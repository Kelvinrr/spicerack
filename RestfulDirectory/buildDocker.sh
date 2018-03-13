docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
docker build -t manager .
docker run -i -p 5000:5000 -v /Users/thatcher/Desktop/Classes/Capstone/spicerack/RestfulDirectory:/app manager
docker attach manager
