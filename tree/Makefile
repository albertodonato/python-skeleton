PYTHON = python3
SETUP = $$(PYTHON) setup.py
LINT = flake8


all: build

build:
	$$(SETUP) build

devel:
	$$(SETUP) develop

clean:
	rm -rf build html *.egg-info

test:
	@$$(SETUP) test

lint:
	@$$(LINT) .

html:
	sphinx-build -b html docs html

.PHONY: build html
