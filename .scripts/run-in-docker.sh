#!/usr/bin/env bash

echo "Seed DB"
python3 manage.py training_sheet_seed
echo "Start email worker"
python3 manage.py rqworker email default &
echo "Start app"
python3 manage.py runserver 0.0.0.0:8000