#!/bin/bash

docker-compose down
docker-compose up -d
docker-compose logs -f app celery
