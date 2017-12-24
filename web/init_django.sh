#!/bin/bash 
#

echo '---------------migrate database main------------------------'
docker exec -it django python manage.py migrate

echo '---------------create superuser admin-----------------------'
docker exec -it django python manage.py createsuperuser --username xx --email xx@qq.com --database default

echo '---------------rebuild index-------------------------------'
docker exec -it django python manage.py rebuild_index
