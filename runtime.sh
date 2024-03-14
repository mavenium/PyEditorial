#!/bin/bash

if command -v docker >/dev/null 2>&1; then
  echo "Docker running"
else
  echo "Please check Docker is installed "
  exit
fi

docker-compose down;
docker-compose build;
docker-compose up -d;

sleep 10

docker-compose exec web python manage.py migrate --noinput

echo "Installation and configuration finished."

