all:	init

init:
	pip install -r requirements.txt

run:
	python src/game.py

test:
	nosetests -v

clean:
	rm -fv src/*.pyc
	rm -fv tests/*.pyc

reset:
	rm -fv score.dat
