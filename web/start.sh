#!/bin/bash 
docker exec -d mysql mysql -uroot -pxxx -e "create database blog;"
docker build -t maybach/django-app .
docker run --name django \
-v /data/docker-django/web/myblog:/usr/src/myblog \
--link mysql:mysql \
-d maybach/django-app /usr/local/bin/uwsgi --http :8000 --chdir /usr/src/myblog -w blogproject.wsgi 

