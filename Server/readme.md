## Build the image using the following command
- docker build -t simple-flask-app:latest .

## Run the Docker container using the command shown below.
- docker run --name test-flask --rm -d -p 5000:5000 simple-flask-app

- docker run --name test-flask --rm -d -p 5000:5000 -v C:\Users\George35mk\Documents\Docker\Tutorials\docker-python\example_3:/code simple-flask-app

- docker run --name test-flask -d -p 5000:5000 -v C:\Users\George35mk\Documents\Docker\Tutorials\docker-python\example_3:/code simple-flask-app


## To stop the container type:
- docker stop test-flask

## To start the container if you dont pass on creation the --rm you can runnit again
- docker start test-flask