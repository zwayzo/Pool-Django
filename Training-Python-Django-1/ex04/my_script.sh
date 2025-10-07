#!/bin/bash
python3 -m venv django_venv
source django_venv/bin/activate
pip install -r requirements.txt
echo "Django environment setup complete."