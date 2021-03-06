# Dominion gRPC client

Client library using the gRPC protocol for the [Dominion](https://github.com/the-gigi/dominion) project

# Build and publish

This section is for the Dominion developers. 
If you just want to implement a player or a client library you can stop reading.

## Pre-requisites

You needto perform these steps just once.

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

## Bump the version

This is important. Whenever you update the package you need to bump the version in setup.py.

## Using the Makefile

Just type `make` and a new package will be built and uploaded to PyPI.

You're done 🎉 !!!

If you want to do it manually follow the rest of this guide.

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
dominion_grpc_client-0.8.0-py3-none-any.whl
```

## Publish the package

Next, we can upload the package using twine to PyPI.

```
(🐙)/dominion-grpc-client-py
$ poetry run twine upload -p ${PYPI_PASSWORD} dist/*.whl

Uploading distributions to https://upload.pypi.org/legacy/
Uploading dominion_grpc_client-0.8.0-py3-none-any.whl
100%|█████████████████████████████| 8.07k/8.07k [00:01<00:00, 4.31kB/s]

View at:
https://pypi.org/project/dominion-grpc-client/0.8/
```
