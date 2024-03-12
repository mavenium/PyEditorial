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
echo "Installation and configuration finished."