# Dominion gRPC client

Client library using the gRPC protocol for the Dominion project

# Build and publish

This section is for the Dominion developers. 
If you just want to implement a player or a client library you can stop reading.

## Pre-requisites

- Install [pyenv](https://github.com/pyenv/pyenv) or [pyenv-win](https://github.com/pyenv-win/pyenv-win)
- Install [poetry](https://python-poetry.org/docs/#installation)

Create a Python 3.8.2 environment

```
$ pyenv install 3.8.2
$ pyenv local
$ poetry init
$ poetry env use 3.8.2
$ poetry install
```

Save the following to ~/.pypirc

```
[distutils]
index-servers=
    pypi
    pypitest

[pypitest]
repository = https://test.pypi.org/legacy/
username = <your user name>

[pypi]
repository = https://pypi.org/legacy/
username = <your user name>
```

## Building the package

Bump the version in setup.py

Here is the command to build the package:

```
(🐙)/dominion-grpc-client-py
$ poetry run python setup.py bdist_wheel
``` 

The result is tar-gzipped file in the dist subdirectory:

```
(🐙)/dominion-grpc-client-py
$ ls dist
dominion_grpc_client-0.6.0-py3-none-any.whl
```

## Publish the package

Next, we can upload the package using twine to PyPI.

```
(🐙)/dominion-grpc-client-py
$ poetry run twine upload -p ${PYPI_PASSWORD} dist/*.whl

Uploading distributions to https://upload.pypi.org/legacy/
Uploading dominion_grpc_client-0.6.0-py3-none-any.whl
100%|█████████████████████████████| 8.07k/8.07k [00:01<00:00, 4.31kB/s]

View at:
https://pypi.org/project/dominion-grpc-client/0.3/
```
