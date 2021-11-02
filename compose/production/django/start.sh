#!/bin/sh
cd /my_blog
python manage_production.py migrate
python manage_production.py collectstatic --noinput
sleep 15
gunicorn blogproject.wsgi:application -w 2 -k gthread -b 0.0.0.0:8000