#!/bin/bash
rm -rf rareapi/migrations
rm db.sqlite3
python manage.py migrate
python manage.py makemigrations rareapi
python manage.py migrate rareapi
python manage.py loaddata users
python manage.py loaddata tokens
python manage.py loaddata categories
python manage.py loaddata rareusers