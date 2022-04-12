#!/usr/bin/env bash
# run with gunicorn (http://docs.gunicorn.org/en/stable/run.html#gunicorn)
exec gunicorn --chdir app  -b :5000 flask-api:app
