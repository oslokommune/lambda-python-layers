.PHONY: pypi
pypi: clean
	python3 setup.py sdist bdist_wheel
	python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/* --verbose

.PHONY: clean
clean:
	rm -rf dist/ build/ bydelsfakta_layer_dataplatform.egg-info