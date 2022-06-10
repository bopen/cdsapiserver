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


image:
	docker build -t $(PROJECT) .

start:
	docker run --rm -ti -v $(PWD):/srv $(PROJECT)
