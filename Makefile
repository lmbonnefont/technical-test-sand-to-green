.PHONY: install test run clean

install:
	pip install -r requirements.txt

test:
	export PYTHONPATH=$PYTHONPATH:. && python3 -m pytest tests/

run:
	export PYTHONPATH=$PYTHONPATH:. && python3 src/main.py

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
