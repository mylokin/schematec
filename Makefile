.PHONY: test clean publish

test:
	flake8 .
	nosetests --with-coverage --cover-package=schematec

clean:
	rm -rf build dist schematec.egg-info

publish: test
	python setup.py sdist bdist_wheel upload
