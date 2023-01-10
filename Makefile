# Makefile to simplify repetitive build env management tasks under posix

CODESPELL_DIRS ?= ./pyaedt
CODESPELL_SKIP ?= "*.pyc,*.xml,*.txt,*.gif,*.png,*.jpg,*.js,*.html,*.doctree,*.ttf,*.woff,*.woff2,*.eot,*.mp4,*.inv,*.pickle,*.ipynb,flycheck*,./.git/*,./.hypothesis/*,*.yml,./docs/build/*,./docs/images/*,./dist/*,*~,.hypothesis*,./docs/source/examples/*,*cover,*.dat,*.mac,\#*,PKG-INFO,*.mypy_cache/*,*.xml,*.aedt,*.svg"
CODESPELL_IGNORE ?= "ignore_words.txt"

all: doctest flake8

doctest: codespell

codespell:
	@echo "Running codespell"
	@codespell $(CODESPELL_DIRS) -S $(CODESPELL_SKIP) # -I $(CODESPELL_IGNORE)

flake8:
	@echo "Running flake8"
	@flake8 .

docker-pull:
	@python -m pip install docker
	@bash .ci/pull_syc_image.sh

build-install:
	@python -m pip install .[build]
	@python -m build
	@python -m pip install -q --force-reinstall dist/*.whl

test-import:
	@python -c "import ansys.systemcoupling.core as pysystemcoupling"

generate-api:
	@echo "Generate API classes"
	@python -m venv env_generate
	@. env_generate/bin/activate
	@python -m pip install -e .
	@python -m pip install .[classesgen]
	@python scripts/generate_datamodel.py
	@rm -rf env_generate

unittest:
	@echo "Running unit tests (including coverage)"
	@python -m pip install .[tests]
	@pytest -v --cov=ansys.systemcoupling --cov-report xml --cov-report html:cov_html --cov-report term:skip-covered --cov-config=.coveragerc
