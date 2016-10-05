run:
	python game/game.py

test:
	nosetests -v

clean:
	rm -fv game/*.pyc
	rm -fv tests/*.pyc

reset:
	rm -fv score.dat
