.PHONY: data test up up-airflow down

data:
	python data/synth/generate.py --out data/synth --seed 42

test:
	python -m pytest -q tests

up:
	docker compose up -d

up-airflow:
	docker compose --profile orchestration up -d

down:
	docker compose --profile orchestration down
