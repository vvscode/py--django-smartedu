python manage.py migrate

# https://docs.djangoproject.com/en/3.0/ref/django-admin/#django-admin-createsuperuser
# DJANGO_SUPERUSER_USERNAME and  DJANGO_SUPERUSER_PASSWORD are used
python manage.py createsuperuser --noinput

python manage.py training_sheet_seed