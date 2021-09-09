FROM nginx:1.21.3-alpine

RUN rm /usr/share/nginx/html/*.html
COPY ./public /usr/share/nginx/html

COPY ./default.conf /etc/nginx/conf.d/default.conf
