#!/usr/bin/env bash
cd ..
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser