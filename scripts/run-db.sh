#!/bin/bash

docker-compose down
docker-compose up -d db redis xnat-db xnat-web xnat-nginx
docker-compose logs -f xnat-web
