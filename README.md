# MovieRater

virtualenv -p /usr/local/bin/python3 venv

souce venv/bin/activate

pip install -r requirements.txt

TO RUN : python3 manage.py runserver

## DB SETUP

Install Postgres
brew services start postgres
psql postgres
CREATE DATABASE movierater;
CREATE ROLE newuser WITH LOGIN PASSWORD 'password'; 
GRANT ALL PRIVILEGES ON DATABASE movierater TO newuser;

python3 manage.py makemigrations
python3 manage.py migrate
