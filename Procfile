release: ./.scripts/release.sh

web: gunicorn smartedu.wsgi

worker: python manage.py rqworker email default