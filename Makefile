VERSION = 0.3

test: lint test-python

develop:
	pip install "flake8>=1.7" --use-mirrors
	pip install ipdb --use-mirrors
	pip install factory_boy
	easy_install readline
	pip install -e . --use-mirrors

test-python:
	@echo "Running Python tests"
	python setup.py -q test || exit 1
	@echo ""

lint: lint-python

lint-python:
	@echo "Linting Python files"
	flake8 --ignore=E111,E121 src/redrover tests || exit 1
	@echo ""