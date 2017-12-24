#!/bin/bash 
#
docker build -t nginx .
docker run --name nginx \
--link django:myblog \
-v /www/static \
--volumes-from django \
-p 80:80 \
-d nginx
