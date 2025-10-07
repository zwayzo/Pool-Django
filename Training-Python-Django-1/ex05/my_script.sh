#!/bin/bash
python3 -m venv django_venv
source django_venv/bin/activate
pip install -r requirements.txt
echo "starting project..."
django-admin startproject mysite
cd mysite
python3 manage.py runserver
python3 manage.py startapp myapp

# echo "Django environment setup complete."