#!/bin/bash 
#
echo "---------------start mysql image-------------------"
docker run --name mysql \
-e MYSQL_ROOT_PASSWORD=xxx \
-p 3306:3306 \
-d daocloud.io/mysql:5.6.30 \
--character-set-server=utf8 --collation-server=utf8_unicode_ci
sleep 15
