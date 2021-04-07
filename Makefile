.DEFAULT_GOAL := all
SHELL = /bin/bash

all: test project

.PHONY: project/install
project/install:
	@poetry install

.PHONY: project/build
project/build:
	@poetry build

.PHONY: project
project: project/build project/install

.PHONY: test
test: test/unit

.PHONY: test/unit
test/unit:
	@poetry run python -m pytest tests/unit
