PYTHON := python3
MANAGE := $(PYTHON) manage.py

.PHONY: help migrate run populate clear_db

help:
	@echo "Usage: make <target>"
	@echo ""
	@echo "Targets:"
	@echo "  migrate        : Run database migrations"
	@echo "  run            : Start Django development server"
	@echo "  populate       : Populate the database with initial data"
	@echo "  clear_db : Empty the database"

migrate:
	@$(MANAGE) makemigrations
	@$(MANAGE) migrate

run:
	@$(MANAGE) runserver

populate:
	@$(MANAGE) populate

clear_db:
	@$(MANAGE) flush
