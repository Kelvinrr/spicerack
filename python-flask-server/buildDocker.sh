# This script builds and runs the flask web app in a docker container
# You will need to set in this file:
#	the path to your SPICE data, 
# 	the path to the swagger_server directory,
# 	and the path to your .ssh directory
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
docker build -t manager .
docker run -it -p 8080:8080 -v ~/Desktop/school/spicerack_withdb/test_concepts/sqlite_db/spice_data:/spicedata/ -v ~/Desktop/school/spicerack_withdb/python-flask-server/swagger_server:/swaggerapp -v ~/.ssh/:/root/.ssh/ manager
docker attach manager
