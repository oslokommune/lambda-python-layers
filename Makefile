.PHONY: build
build:
	sh build.sh pandas_layer
	sh build.sh s3_layer


.PHONY: sls
sls:
	sls deploy

.PHONY: deploy
deploy: build sls