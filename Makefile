PYTHONPATH ?= $(pwd)

.PHONY: run state_space lint

run:
	@python -m app.tic_tac_toe.main

state_space:
	@python -m app.state_space.main

lint:
	@pylint --ignore=.venv .
