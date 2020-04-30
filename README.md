# SmartEdu - Django Playground

This site is based on Django 3 for "Python Web-developer" OTUS course.

It uses [`pipenv`](https://webdevblog.ru/pipenv-rukovodstvo-po-novomu-instrumentu-python/). So to setup environment you need first install `pipenv`. And after that:

1. Clone repository
2. Go to project directory and run `pipenv install`

## Basic operations:

Before all run `pipenv shell` and continue in created shell.


Run server locally:
```
python manage.py runserver
```


Apply migrations:
```
python manage.py migrate
```

**Data operations** (check this [link](https://coderwall.com/p/mvsoyg/django-dumpdata-and-loaddata) for more options)

Save data from DB to file: 
```
python manage.py dumpdata > db.json
```


Load data from file:
```
python manage.py loaddata db.json
```