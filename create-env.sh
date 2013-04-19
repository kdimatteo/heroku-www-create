#!/bin/bash

virtualenv venv --distribute
source venv/bin/activate
pip install Flask

echo "web: python server.py" > Procfile

pip freeze > requirements.txt