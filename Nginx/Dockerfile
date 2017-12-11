FROM nginx:1.13.7-alpine
MAINTAINER Georgios Chatoutsidis "george35mk@gmail.com"
RUN rm /etc/nginx/nginx.conf
COPY ./Nginx/nginx.conf /etc/nginx/nginx.conf
COPY ./Client/dist /usr/share/nginx/html
EXPOSE 80