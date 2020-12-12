all:
	rm -rf dist
	poetry run python setup.py bdist_wheel
	poetry run twine upload -p ${PYPI_PASSWORD} dist/*.whl
