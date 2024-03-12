#!/bin/bash

python manage.py makemigrations content
python manage.py migrate
python manage.py collectstatic --noinput


     