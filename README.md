# my-first-blog
Learning Django through the [Django Girls tutorial](https://tutorial.djangogirls.org/en/).

Project dependencies:

- python
- django
- psycopg2
- docker (container for the postgreSQL database)

How to run:

```sh
python -m venv .venv
source .venv/bin/activate # linux
```

```sh
pip install -U pip
pip install -r requirements.txt
```

The easiest way to create the database is in a docker container:

```sh
docker run --name postgres -e POSTGRES_PASSWORD=123 -d -p 5432:5432 postgres

# docker run --name <container-name-of-your-choice> -e POSTGRES_PASSWORD=<password> -d -p 5432:5432 postgres:<image-version>
```

Enter the container to create the database:

```sh
docker exec -it postgres bash # docker exec -it <container-name> bash

psql -U postgres # psql -U <user>

CREATE DATABASE djangu; # if you chose a different container name, be sure to change it on mysite/settings.py

\q
exit
```

```sh
python manage.py migrate # create database migrations
python manage.py createsuperuser # fill in the user and password fields
python manage.py runserver # runs on https://localhost:8000/
```
