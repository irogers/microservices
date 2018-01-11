
docker-compose -f docker-compose-dev.yml up -d --build

Recreate Database

``` bash
$ docker-compose -f docker-compose-dev.yml run users-service python manage.py recreate_db
```

Connect to Database

``` bash
$ docker exec -ti $(docker ps -aqf "name=users-db") psql -U postgres

# \c users_dev
# \dt
# \q
```

Run tests
``` bash
$ docker-compose -f docker-compose-dev.yml run users-service python manage.py test
```