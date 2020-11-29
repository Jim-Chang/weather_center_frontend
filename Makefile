.DEFAULT_GOAL := help
.PHONY: help
SERVICE_NAME = chatbot-service
DB_SERVICE_NAME = chatbot-db
DB_USER = chatbot
WORK_DIR = app

## Start container for develop
develop:
	docker-compose -f docker-compose.develop.yml up -d

## Migrate chatbot db
migrate:
	docker exec -it $(SERVICE_NAME) sh -c 'alembic -c /app/db/migrations/alembic.ini upgrade head'

## Revision service db, ex: make revision MSG=init
revision:
	docker exec -it $(SERVICE_NAME) sh -c 'alembic -c /app/db/migrations/alembic.ini revision --autogenerate -m "$(MSG)"'

## Healthcheck for manually
healthcheck:
	docker exec -it $(SERVICE_NAME) sh -c 'python check_health.py'

## Go container console
console:
	docker exec -it $(SERVICE_NAME) /bin/bash

## Go container console with superuser
su:
	docker exec -it -u root $(SERVICE_NAME) /bin/bash

## Go db, ONLY FOR LOCAL!!
db-local:
	docker exec -it $(DB_SERVICE_NAME) sh -c 'psql -U $(DB_USER)'

## init h2-test db for test, ONLY FOR LOCAL or CI!!
init-h2-test-db:
	bash app/tests/scripts/create_h2_test_db.sh

## Get logs
logs:
	docker logs -f $(SERVICE_NAME)

## Build proto files
build-proto:
	docker exec -i $(SERVICE_NAME) sh -c 'python -m grpc_tools.protoc -I ./proto/ --python_out=./proto/pb/ --grpc_python_out=./proto/pb/ ./proto/*.proto'

## Build service image
build-image:
	docker build -t $(SERVICE_NAME):latest .

## Delete local container
clean-local:
	# del docker container 
	make stop-local
	# del image 
	docker rmi -f $(SERVICE_NAME):$(IMAGE_VERSION)

## Delete dev container
clean-dev:
	# del docker container 
	make stop-dev
	# del image 
	docker rmi -f $(SERVICE_NAME):$(IMAGE_VERSION)

## Delete prod container
clean:
	# del docker container 
	make stop
	# del image 
	docker rmi -f $(SERVICE_NAME):$(IMAGE_VERSION)

## Start for local
start-local:
	docker-compose -f docker-compose.local.yml up -d
	
## Stop for local
stop-local:
	docker-compose -f docker-compose.local.yml down

help:
	$(info Available targets)
	@awk '/^[a-zA-Z\-\_0-9]+:/ {                                   \
	  nb = sub( /^## /, "", helpMsg );                             \
	  if(nb == 0) {                                                \
	    helpMsg = $$0;                                             \
	    nb = sub( /^[^:]*:.* ## /, "", helpMsg );                  \
	  }                                                            \
	  if (nb)                                                      \
	    printf "\033[1;31m%-" width "s\033[0m %s\n", $$1, helpMsg; \
	}                                                              \
	{ helpMsg = $$0 }'                                             \
	width=$$(grep -o '^[a-zA-Z_0-9]\+:' $(MAKEFILE_LIST) | wc -L)  \
	$(MAKEFILE_LIST)
