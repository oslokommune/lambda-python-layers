.PHONY: build
build:
	sh build.sh pandas_layer
	sh build.sh s3_layer
	sh build.sh bydelsfakta_layer


.PHONY: sls
sls:
	sls deploy

.PHONY: deploy
deploy: build sls


.PHONY: pypi
pypi:
	python3 setup.py sdist bdist_wheel &&\
	python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*