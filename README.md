# MovieRater

- Setup virtual environment<br>
    ```virtualenv -p /usr/local/bin/python3 venv```
- Activate virtual environment <br>
    ```souce venv/bin/activate```
- Install all the requirements <br>
    ```pip install -r requirements.txt```
- Run the application <br>
    ```python3 manage.py runserver```

### DB SETUP

- Install Postgres <br>
- Start postgres <br>
    ```brew services start postgres```
- Enter postgres Console <br>
    ```psql postgres```
- Create Database <br>
    ```CREATE DATABASE movierater;```
- Create a new Role <br> 
    ```CREATE ROLE newuser WITH LOGIN PASSWORD 'password';```
- Grant the privileges to the created role <br>
    ```GRANT ALL PRIVILEGES ON DATABASE movierater TO newuser;```
- Make and run migrations on the Database. <br>
    ```python3 manage.py makemigrations``` <br>
    ```python3 manage.py migrate```
