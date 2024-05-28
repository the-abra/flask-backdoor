#!/bin/bash

source src/functions.sh

if ! command -v nginx; then
    source setup/setup.sh
fi

service nginx start
cd core/
python app.py
cd ..