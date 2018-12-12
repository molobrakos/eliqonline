default: check

black:
	white . eliqonline

clean:
	rm -rf dist *.egg-info .pytest_cache __pycache__
	find . -name '*.pyc' -exec rm -f {} \;
	find . -name '*.pyo' -exec rm -f {} \;
	find . -name '*~' -exec rm -f {} \;

lint: requirements.txt setup.py
	tox -e lint

test: requirements.txt setup.py
	tox

check: lint test

pypitest:
	python setup.py sdist
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

pypi:
	python setup.py sdist
	twine upload dist/*

release:
	git diff-index --quiet HEAD -- && make check && bumpversion patch && git push --tags && git push && make pypi


run:
	@python -m eliqonline -vv now
