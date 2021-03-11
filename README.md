# Taucher karten 


## Actual setup doc
- install python3 with dev
    - `sudo apt install python3 python3-dev`
- install mariadb database
    - `sudo apt install mariadb-server`
    - you should secure the installation by password etc:
    - `sudo mysql_secure_installation`
    - ... TODO permissions for user
- setup venv `python3 -m virtualenv venv`
- activate venv `source venv/bin/activate`
- install deps `python3 -m pip install -r requirements.txt`

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
