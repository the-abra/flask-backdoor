#!/bin/bash

source src/functions.sh

if ! command -v nginx; then
    source setup/setup.sh
fi

python core/host.py