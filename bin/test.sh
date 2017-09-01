#!/bin/bash

source .env/bin/activate
nosetests -v --with-coverage --nocapture --cover-package=game,apple,snake
deactivate
