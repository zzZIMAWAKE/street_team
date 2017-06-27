VENV ?= ./.virtualenv

test:
	$(VENV)/bin/nosetests

install:
	python3 -m venv $(VENV) && \
	$(VENV)/bin/pip install -r requirements.txt

services:
	docker-compose up

setup_db:
	$(VENV)/bin/alembic upgrade head

rabbit:
	docker-compose up rabbit

postgresql:
	docker-compose up postgres

sales:
	$(VENV)/bin/python3 src/sales_service.py

rewards:
	$(VENV)/bin/python3 src/rewards_service.py
