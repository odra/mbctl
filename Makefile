SHELL = /bin/bash


.PHONY: test
test: test/unit

.PHONY: test/unit
test/unit:
	@poetry run python -m pytest tests/unit
