# Latest at time of creation: "1.19.6"; use "1.19" to get bugfixes. If NGINX
# uses semver, "1" should be safe, too.
FROM nginx:1.19


# Make a self-signed cert available in case the config uses SSL
RUN mkdir /cert
COPY ./openssl.conf .
RUN openssl req -x509 -nodes -days 3650 -newkey rsa:2048 -config openssl.conf \
    -keyout /cert/ssl.key -out /cert/ssl.crt

RUN rm /usr/share/nginx/html/*
# TODO: Consider baking the full config in the image instead of using compose? ¯\_(ツ)_/¯
