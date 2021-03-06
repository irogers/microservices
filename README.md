# Microservices with Docker, Flask, and React

[![Build Status](https://travis-ci.org/irogers/microservices.svg?branch=master)](https://travis-ci.org/irogers/microservices)


## Build

Using either `dev` or `prod`
``` bash
docker-compose -f docker-compose-prod.yml up -d --build

docker-compose -f docker-compose-prod.yml \
  run users-service python manage.py recreate_db

docker-compose -f docker-compose-prod.yml \
  run users-service python manage.py seed_db

docker-compose -f docker-compose-prod.yml \
  run users-service python manage.py test
```
## Update

After installing a new dependency:
```
docker-compose -f docker-compose-prod.yml up -d --build
```

## Stop the containers

```
docker-compose -f docker-compose-dev.yml stop
docker-compose -f docker-compose-dev.yml down
```

## Check code coverage and quality

```
docker-compose -f docker-compose-dev.yml   run users-service python manage.py cov
docker-compose -f docker-compose-dev.yml   run users-service flake8 project
```

## Connect to Database

``` bash
$ docker exec -ti $(docker ps -aqf "name=users-db") psql -U postgres
```
Then, you can connect to the database and run SQL-queries. For example:

``` bash
# \c users_dev
# select * from users
# \dt
# \q
```