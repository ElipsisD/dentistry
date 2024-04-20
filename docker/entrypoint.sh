server() {
  echo "Migrate..."
  python ./manage.py migrate --noinput

  echo "Collect static"
  python ./manage.py collectstatic --noinput
  
  echo "Run server..."
  gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 2 --timeout 600 --reload
}

$1
