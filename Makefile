install:
	poetry install
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --user dist/*.whl
lint:
	poetry run flake8 brain_games
run-games:
	poetry run python -m brain_games.scripts.brain_games
run-even:
	poetry run python -m brain_games.scripts.brain_even
run-calc:
	poetry run python -m brain_games.scripts.brain_calc
run-gcd:
	poetry run python -m brain_games.scripts.brain_gcd
run-progression:
	poetry run python -m brain_games.scripts.brain_progression
run-prime:
	poetry run python -m brain_games.scripts.brain_prime
