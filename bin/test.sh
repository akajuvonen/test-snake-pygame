#!/bin/bash

source .env/bin/activate
nosetests -v --with-coverage --cover-package=game,apple,snake
deactivate
