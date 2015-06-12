.PHONY: test clean publish

test:
	flake8 .
	python -m pytest --cov-report term-missing --cov schematec

clean:
	rm -rf build dist schematec.egg-info

publish: test
	git push
	python setup.py sdist bdist_wheel upload
