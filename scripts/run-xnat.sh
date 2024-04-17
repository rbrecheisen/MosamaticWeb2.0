#!/bin/bash

cd xnat
docker-compose down
docker-compose up -d && docker-compose logs -f
