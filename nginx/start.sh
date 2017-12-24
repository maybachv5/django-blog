#!/bin/bash 
#
docker build -t nginx .
docker run --name nginx \
--link django:myblog \
-v /data/docker-django/nginx/ssl:/etc/nginx/ssl \
--volumes-from django \
-p 80:80 \
-p 443:443 \
-d nginx
