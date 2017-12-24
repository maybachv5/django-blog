# django-blog

django-blog/mysql/start.sh 
	#-e MYSQL_ROOT_PASSWORD=xxx \
  
django-blog/web/start.sh
	#docker exec -d mysql mysql -uroot -pxxx -e "create database blog;"
	
django-blog/web/init_django.sh
	#docker exec -it django python manage.py createsuperuser --username xx --email xx@qq.com --database default
	
django-blog/web/myblog/blogproject/settings.py
	#ALLOWED_HOSTS = ['www.xxx.com']
    #'PASSWORD':'xxx',
