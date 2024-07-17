#!/bin/bash

mkdir venv && \
python -m venv ./venv && \
source ./venv/bin/activate && \

pip install -r .requirements.txt && \
python manage.py migrate --noinput && \
# Only for PROD
# python manage.py collectstatic --noinput && \
python manage.py runserver
