#!/bin/bash

set -e

echo "Waiting for database..."
while ! nc -z ${DB_HOST} ${DB_PORT}; do sleep 1; done
echo "Connected to database."

python manage.py migrate --no-input
status=$?
if [ $status -ne 0 ]; then
  echo "Failed to migrate database: $status"
  exit $status
fi

python manage.py compilemessages
status=$?
if [ $status -ne 0 ]; then
  echo "Failed to compilemessages: $status"
  exit $status
fi

python manage.py collectstatic --no-input
status=$?
if [ $status -ne 0 ]; then
  echo "Failed to collect staticfiles: $status"
  exit $status
fi

gunicorn boilerplate.wsgi:application \
  --name boilerplate-gunicorn \
  --bind 0.0.0.0:8000 \
  --workers 10 \
  --pythonpath "/opt/app/src" \
  --log-level=debug \
  --timeout 120 \
  --reload
status=$?
if [ $status -ne 0 ]; then
  echo "Failed to start gunicorn: $status"
  exit $status
fi
