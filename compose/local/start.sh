#!/bin/sh
python manage_local.py migrate
python manage_local.py runserver 0.0.0.0:8000
