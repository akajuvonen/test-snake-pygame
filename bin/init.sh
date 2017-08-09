#!/bin/bash

if [ ! -d .env ]; then
  virtualenv .env --no-site-packages
  source .env/bin/activate
  pip install -r requirements.txt
  deactivate
fi;
