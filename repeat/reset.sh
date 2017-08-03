#!/usr/bin/env bash

# Destroy the current database. For development purposes only!

maybe_delete () { ([[ -f "$1" ]] || [[ -d "$1" ]]) && rm -rf "$1"; }

maybe_delete api/migrations
maybe_delete db.sqlite3
maybe_delete /tmp/repeat.sqlite3
./manage.py makemigrations
./manage.py migrate --run-syncdb
./manage.py loaddata ./api/fixtures/fixture.json
./manage.py createsuperuser
