#!/bin/sh
cd /my_blog
sleep 60    #停止60秒等待mysql容器初始化完成否则启动应用会报连接错误
python manage_production.py makemigrations
python manage_production.py migrate
python manage_production.py collectstatic --noinput
gunicorn blogproject.wsgi:application -w 2 -k gthread -b 0.0.0.0:8000