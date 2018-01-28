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
## Connect to Database

``` bash
$ docker exec -ti $(docker ps -aqf "name=users-db") psql -U postgres

# \c users_dev
# \dt
# \q
```