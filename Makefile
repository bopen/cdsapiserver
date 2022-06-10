PROJECT := cdsapiserver
CONDA := conda
CONDAFLAGS :=
COV_REPORT := html

default: qa test

qa:
	pre-commit run --all-files

test:
	python -m pytest -vv --cov=. --cov-report=$(COV_REPORT)

type-check:
	python -m mypy --strict .

conda-env-update:
	$(CONDA) env update $(CONDAFLAGS) -f environment.yml

docker-build:
	docker build -t $(PROJECT) .

docker-run:
	docker run --rm -ti -v $(PWD):/srv $(PROJECT)

# local targets

start:
	uvicorn --reload --log-level info --workers 1 cdsapiserver:app
