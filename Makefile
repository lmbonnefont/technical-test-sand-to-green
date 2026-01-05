.PHONY: install test run clean

install:
	pip install -r requirements.txt

test:
	pytest tests/

run:
	python3 -m src.main

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
