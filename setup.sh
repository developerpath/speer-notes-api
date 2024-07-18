#!/bin/bash

env=$1;

rm venv -rf && \
mkdir venv && \
python -m venv ./venv && \
source ./venv/bin/activate && \

pip install -r requirements.txt

if [ $env != 'prod' ]; then
    touch db.sqlite3
fi

python manage.py migrate --noinput

if [ $env == 'prod' ]; then
    python manage.py collectstatic --noinput
else
    python manage.py runserver
fi
