# test-snake-pygame
A simple snake-like game with PyGame. Made to test and demonstrate pygame-related features, such as game event loop, drawing to the screen etc.

Apples appear randomly. High-score is saved to a file using pickle, and it is loaded if file is available.

## Dependencies

You only need python, virtualenv and pip. Then create a new virtual environment, and inside that run `make init`. This will pull the necessary dependencies from requirements file using pip. The required packages are listed in `requirements.txt`.

## Tests

If you want, you can run the unit tests with `make test`. The tests use nose, which is installed to virtualenv when initializing from the makefile.

## Running

Just type `make run`.

## Cleaning up

If you want to get rid of the pyc files, you can do so with `make clean`.
