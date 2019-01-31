import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bydelsfakta_layer_dataplatform",
    version="0.0.3",
    author="tordsk",
    author_email="dataplatform@byr.oslo.kommune.no",
    description="A small example package",
    long_description=long_description,
    url="https://github.com/oslokommune/lambda-python-layers",
    py_modules=["bydelsfakta_layer"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)