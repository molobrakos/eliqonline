help:
	@echo "  ___ _ _       ___       _ _            _   ___ ___ "
	@echo " | __| (_)__ _ / _ \ _ _ | (_)_ _  ___  /_\ | _ \_ _|"
	@echo " | _|| | / _' | (_) | ' \| | | ' \/ -_)/ _ \|  _/| | " 
	@echo " |___|_|_\__, |\___/|_||_|_|_|_||_\___/_/ \_\_| |___|"
	@echo "            |_| Python Libary                        "
	@echo "make.."
	@echo "      clean: clean project"
	@echo "      pep8: run flake8 (pep8) on project"
	@echo "      lint: run pylint on project"
	@echo "      push: push to master"
	@echo "      test: run tests"
	@echo ""

clean:
	find . -name '*.pyc' -exec rm -f {} \;
	find . -name '*.pyo' -exec rm -f {} \;
	find . -name '*~' -exec rm -f {} \;

pep8:
	flake8 eliqonline

lint:
	pylint -E eliqonline

push:
	git push -u origin master

test:
	nosetests -v

