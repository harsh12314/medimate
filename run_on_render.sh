#!/usr/bin/env bash
echo "Applying migrations..."
python manage.py migrate --noinput

echo "Starting server..."
gunicorn medimate.wsgi:application --bind 0.0.0.0:$PORT
