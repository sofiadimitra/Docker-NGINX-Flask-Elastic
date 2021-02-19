## Docker-NGINX-FLASK-ELASTIC
This is a Docker image for Nginx + Flask + Elasticsearch

### Run and Build the image with this command:
- docker-compose up --build 

### Stop the image with this command:
- docker-compose stop 

### Stop and Remove the image with this command:
This command wille stop the instance and is gonna delete the containers
- docker-compose down 

### Dependencies
- Nginx:1.13.7-alpine 
- Python:3.6.3
- Elasticsearch:6.0.1


## My folder structure

> My folder structure

    app
    |__Client
    |   |__dist
    |      |__index.html
    |
    |__Nginx
    |   |__Dockerfile
    |   |__nginx.conf
    |
    |__Server
    |   |__api.py
    |   |__Dockerfile
    |   |__requirement.txt
    |
    |__Elasticsearch
    |   |__config
    |   |   |__elasticsearch.yml
    |   |
    |   |__Dockerfile
    |
    |__docker-compose.yml
    
