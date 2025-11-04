.PHONY: etl features train forecast evaluate all
PY=python
etl:
	$(PY) -m src.etl
features:
	$(PY) -m src.features
train:
	$(PY) -m src.train
forecast:
	$(PY) -m src.forecast
evaluate:
	$(PY) -m src.evaluate
all: etl features train evaluate forecast
