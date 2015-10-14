help:
	@echo "- clean"
	@echo "- pep8"
	@echo "- lint"

clean:
	find . -name '*.pyc' -exec rm -f {} \;
	find . -name '*.pyo' -exec rm -f {} \;
	find . -name '*~' -exec rm -f {} \;

pep8:
	flake8 eliqonline

lint:
	pylint -E eliqonline
