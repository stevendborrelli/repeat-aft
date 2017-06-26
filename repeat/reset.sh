#!/usr/bin/env bash

# Destroy the current database. For development purposes only!

rm -rf api/migrations
rm -f db.sqlite3
./manage.py makemigrations
./manage.py migrate --run-syncdb
