install:
	poetry install
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --user dist/*.whl
package-reinstall:
	python3 -m pip install --force-reinstall --user dist/*whl
lint:
	poetry run flake8 brain_games
brain-games:
	poetry run brain-games
brain-even:
	poetry run brain-even
brain-calc:
	poetry run brain-calc
run-games:
	poetry run python -m brain_games.scripts.brain_games
run-even:
	poetry run python -m brain_games.scripts.brain_even
run-calc:
	poetry run python -m brain_games.scripts.brain_calc
