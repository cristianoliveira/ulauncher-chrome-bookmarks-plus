.PHONY: help
help: ## Lists the available commands. Add a comment with '##' to describe a command.
	@grep -E '^[a-zA-Z_-].+:.*?## .*$$' $(MAKEFILE_LIST)\
		| sort\
		| awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: install
install: ## Install ulauncher extension
	ln -sf $(shell pwd) ~/.local/share/ulauncher/extensions/

.PHONY: setup
setup: install ## Setup extension in ~/.local/share/ulauncher/extensions/
	python -m venv .venv
	source .venv/bin/activate
	pip install -r requirements.txt

.PHONY: test
test: ## Run tests using pytest
	python -m unittest discover -s tests

.PHONY: start
start: ## Attemps to kill current ulauncher process and starts a new one.
	ps aux | grep ulauncher | grep -v grep | awk '{print $$2}' | xargs kill -9
	ulauncher --no-extensions --dev -v > /tmp/ulauncher.log 2>&1 &
	sleep 2
	python main.py

	# truncate -s 0 ulauncher.log
	# tail -f ulauncher.log

.PHONY: stop
stop: ## Stop ulauncher process
	ps aux | grep ulauncher | grep -v grep | awk '{print $$2}' | xargs kill -9

.PHONY: lint
lint: ## Check code style using flake8
	ruff check

.PHONY: format
format: ## Format code using black
	ruff check --fix
	ruff format
