VENV ?= ./.virtualenv

test:
	$(VENV)/bin/nosetests

install:
	python3 -m venv $(VENV) && \
	$(VENV)/bin/pip install -r requirements.txt
	$(VENV)/bin/alembic upgrade head

services:
	docker-compose up

rabbit:
	docker-compose up rabbit

postgres:
	docker-compose up postgres

sales:
	$(VENV)/bin/python3 src/sales_service.py

rewards:
	$(VENV)/bin/python3 src/rewards_service.py
