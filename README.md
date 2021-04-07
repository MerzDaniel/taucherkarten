# Taucher karten 

## Lage page PLAN
main data:
- (Picture)
- Map (openstreet)
    - location
    - deepness
    - POIs
- Info
    - 
- Links
    - Wikipedia
    - seen.de
    - taucher info
    - https://tauchplatzkarten.de/shop (Kooperation)
    
### Divespot
- Description
- Map

## Actual setup doc
- install python3 with dev
    - `sudo apt install python3 python3-dev`
- setup venv `python3 -m virtualenv venv`
- activate venv `source venv/bin/activate`
- install deps `python3 -m pip install -r requirements.txt`
    - (it could be that mod_wsgi needs to be installed globally. It is needed for the server startup)
- startup DB `docker-compose up -d`
- db migrations 
- load initial data `python manage.py loaddata lakes`
- start server `python manage.py runserver`

### Various stuff
- Make devserver reachable from other computer `python manage.py runserver 0.0.0.0:8000`

### Mysql db 
If you'd like to setup DB locally (not in docker):

- install mariadb database
    - `sudo apt install mariadb-server`
    - you should secure the installation by password etc:
    - `sudo mysql_secure_installation`
    - ... TODO permissions for user

## Obscure setup doc
- start mysql
- secure install
- django 
- graphene
- ...

source env/bin/activate
sudo service mysql start
python manage.py runserver
python manage.py makemigrations
python manage.py migrate
./manage.py createsuperuser

// create db
 create database divemaps character set utf8;
grant ALL on divemaps . * to 'daniel'@'localhost';
flush privileges;python manage.py collectstatic --no-input
python manage.py runmodwsgi
