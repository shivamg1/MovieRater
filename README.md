# MovieRater

## Running the application: 
- Setup virtual environment<br>
    ```commandline
    virtualenv -p /usr/local/bin/python3 venv
- Activate virtual environment <br>
    ```commandline
    souce venv/bin/activate
- Install all the requirements <br>
    ```commandline
    pip install -r requirements.txt
- __Setup Database__

- Run the application <br>
    ```commandline
    python3 manage.py runserver
    
- To run the test cases <br>
    ```commandline
    python3 manage.py test rating.tests

- To add the Cron Job <br>
    ```commandline
    python3 manage.py crontab add

### DB SETUP

- Install Postgres <br>
- Start postgres <br>
    ```commandline
    brew services start postgres
- Enter postgres Console <br>
    ```commandline
    psql postgres
- Create Database <br>
    ```commandline
    CREATE DATABASE movierater;
- Create a new Role <br> 
    ```commandline
    CREATE ROLE newuser WITH LOGIN PASSWORD 'password';
- Grant the privileges to the created role <br>
    ```commandline
    GRANT ALL PRIVILEGES ON DATABASE movierater TO newuser;
- Make and run migrations on the Database. <br>
    ```commandline
    python3 manage.py makemigrations
    python3 manage.py migrate
