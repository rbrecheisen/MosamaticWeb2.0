#!/bin/bash

python manage.py makemigrations
python manage.py migrate
# python manage.py initialize_periodic_tasks

gunicorn mosamaticweb.wsgi:application --bind 0.0.0.0:8000