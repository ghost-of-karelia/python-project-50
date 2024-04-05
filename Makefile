build:
	poetry build

install:
	poetry install

package-install:
	python3 -m pip install dist/*.whl --force-reinstall

lint:
	poetry run flake8 gendiff