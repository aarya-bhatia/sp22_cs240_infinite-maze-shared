#! /bin/bash

cd $1;
export FLASK_ENV=production
python3 -m flask run --host=0.0.0.0