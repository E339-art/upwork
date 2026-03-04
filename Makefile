.PHONY: install lint format test all clean help

help: ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'

install: ## Install all dependencies
	pip install -r requirements.txt

lint: ## Run linters (Ruff + Black check)
	python -m ruff check src/ tests/
	python -m black --check src/ tests/

format: ## Auto-format code with Black and Ruff
	python -m black src/ tests/
	python -m ruff check --fix src/ tests/

test: ## Run test suite with Pytest
	python -m pytest tests/ -v --tb=short

coverage: ## Run tests with coverage report
	python -m pytest tests/ -v --cov=src --cov-report=term-missing

all: lint test ## Run lint and test

clean: ## Remove build artifacts and caches
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .pytest_cache -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .ruff_cache -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	rm -rf build/ dist/ *.egg-info/ .coverage htmlcov/
