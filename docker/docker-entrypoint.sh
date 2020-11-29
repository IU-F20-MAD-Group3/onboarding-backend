#!/usr/bin/env sh

set -e

: "${DJANGO_APP_NAME:?DJANGO_APP_NAME is missing}"

: "${DJANGO_DATABASE_HOST:?DJANGO_DATABASE_HOST is missing}"
: "${DJANGO_DATABASE_PORT:?DJANGO_DATABASE_PORT is missing}"

echo "Waiting for database to start..."
while ! nc -z "$DJANGO_DATABASE_HOST" "$DJANGO_DATABASE_PORT"; do
  sleep 1
done
echo "done"
echo

echo "Making database migrations..."
python manage.py makemigrations
echo "done"
echo

echo "Applying database migrations..."
python manage.py migrate
echo "done"
echo

echo "Collecting static files..."
python manage.py collectstatic --no-input
echo "done"
echo

HOST="0.0.0.0"
PORT="8000"

if [ "$1" = "uwsgi" ]; then
  : "${UWSGI_PROCESSES:?UWSGI_PROCESSES is missing}"
  : "${UWSGI_THREADS:?UWSGI_THREADS is missing}"

  echo "Starting uwsgi..."
  exec "$@" \
    --module="$DJANGO_APP_NAME".wsgi:application \
    --processes="$UWSGI_PROCESSES" \
    --threads="$UWSGI_THREADS" \
    --http-socket="$HOST:$PORT" \
    --static-map /static=/data/static \
    --log-x-forwarded-for
elif [ "$1" = "devserver" ]; then
  echo "Starting a development server..."
  exec python manage.py runserver "$HOST:$PORT"
fi

exec "$@"
