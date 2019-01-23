#!/bin/sh

cd $1
export PKG_DIR="python" # Must be python or python/lib/python3.7/site-packages

rm -rf ${PKG_DIR} && mkdir -p ${PKG_DIR}

docker run --rm -v $(pwd):/foo -w /foo lambci/lambda:build-python3.7 \
    pip install -r requirements.txt --no-deps -t ${PKG_DIR}

