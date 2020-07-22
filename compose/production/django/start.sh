#!/bin/sh
python manage_production.py migrate
python manage_production.py collectstatic --noinput
gunicorn blogproject.wsgi:application -w 4 -k gthread -b 0.0.0.0:8000 --chdir=/Myblog