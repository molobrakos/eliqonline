help:
	@echo "  ___ _ _       ___       _ _            _   ___ ___ "
	@echo " | __| (_)__ _ / _ \ _ _ | (_)_ _  ___  /_\ | _ \_ _|"
	@echo " | _|| | / _' | (_) | ' \| | | ' \/ -_)/ _ \|  _/| | " 
	@echo " |___|_|_\__, |\___/|_||_|_|_|_||_\___/_/ \_\_| |___|"
	@echo "            |_| Python Library                        "
	@echo "make:"
	@echo "      clean: clean project"
	@echo "      pep8: run flake8 (pep8) on project"
	@echo "      lint: run pylint on project"
	@echo "      test: run tests"
	@echo "      pypi: register and upload to pypi"
	@echo "      pypitest: register and upload to pypitest"
	@echo ""

clean:
	rm -rf dist
	find . -name '*.pyc' -exec rm -f {} \;
	find . -name '*.pyo' -exec rm -f {} \;
	find . -name '*~' -exec rm -f {} \;

pep8:
	flake8 eliqonline

lint:
	pylint -E eliqonline

test:
	nosetests --with-coverage --cover-package eliqonline 

pypitest:
	python setup.py register -r pypitest
	python setup.py sdist upload -r pypitest

pypi:
	python setup.py register -r pypi
	python setup.py sdist upload -r pypi


