import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pandas_layer_dataplatform",
    version="0.0.3",
    author="tordsk",
    author_email="dataplatform@byr.oslo.kommune.no",
    description="A small example package",
    long_description=long_description,
    url="https://github.com/oslokommune/lambda-python-layers",
    py_modules=["pandas_layer"],
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
)
