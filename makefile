VENV = .venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

.PHONY: run clean cleancache devenv


$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt

run: $(VENV)/bin/activate
	$(PYTHON) cli.py 2023

cleancache:
	find . -name "__pycache__" -exec rm -rf {} +
	rm -rf .pytest_cache
	rm -rf .ruff_cache

clean: cleancache
	rm -rf $(VENV)
	rm -rf .tox
	rm -rf .pre-commit-config.yaml tox.ini pytest.ini
	rm -rf dist retailcalendar.egg-info

devenv: $(VENV)/bin/activate tox.ini pytest.ini .pre-commit-config.yaml
	$(PIP) install black pre-commit pydocstyle pytest pytest-clarity pytest-dotenv tox ruff httpx isort sourcery
	if [ ! -d ".git" ]; then git init; fi
	pre-commit install

precommit: devenv
	black .
	ruff . --fix
	pre-commit run --all-files
	tox

build: $(VENV)/bin/activate
	$(PYTHON) -m pip install --upgrade build
	$(PYTHON) -m build

protobuf:
	wget https://github.com/protocolbuffers/protobuf/releases/download/v24.0/protoc-24.0-linux-x86_64.zip
	unzip -j protoc-24.0-linux-x86_64.zip bin/protoc -d src/protobuff/
	chmod 755 src/protobuff/protoc
	src/protobuff/protoc --python_out=. src/protobuff/gauth.proto
	rm protoc-24.0-linux-x86_64.zip src/protobuff/protoc

include files.mk
