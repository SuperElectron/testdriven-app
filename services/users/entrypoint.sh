#!/bin/sh

echo "Waiting for MongoDB to start..."

while ! nc -z users-db 27017; do
  sleep 0.1
done

echo "MongoDb started."

python manage.py run -h 0.0.0.0