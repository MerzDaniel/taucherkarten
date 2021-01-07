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
