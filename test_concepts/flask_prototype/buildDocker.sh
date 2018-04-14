docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
docker build -t manager .
docker run -it -p 5000:5000 -v /Users/thatcher/Desktop/Classes/Capstone/spicerack/RestfulDirectory:/app -v /Users/thatcher/.ssh/:/root/.ssh/ manager
docker attach manager
