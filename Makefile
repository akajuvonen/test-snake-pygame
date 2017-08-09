all:	init

init:
	bin/init.sh

test:
	bin/init.sh
	bin/test.sh

run:
	bin/init.sh
	bin/run.sh

clean:
	rm -fv *.pyc
	rm -fv tests/*.pyc
	rm -fv config/*.pyc
	rm -rfv .env/
	rm -fv .coverage
