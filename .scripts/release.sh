#!/usr/bin/env bash

python manage.py flush

rm -rf db.sqlite3

python manage.py migrate

# https://docs.djangoproject.com/en/3.0/ref/django-admin/#django-admin-createsuperuser
# DJANGO_SUPERUSER_USERNAME and  DJANGO_SUPERUSER_PASSWORD, DJANGO_SUPERUSER_EMAIL are used
python manage.py createsuperuser --noinput --email $DJANGO_SUPERUSER_EMAIL

python manage.py training_sheet_seed