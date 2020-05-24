## API Endpoints

### 1. /signup
   POST<br>
   Creates a new user with the details provided.
   <br>
   No Authentication Required 
   <br>
   Arguments: 
   - first_name : String
   - last_name : String
   - email : String
   - password : String
   
   Returns:
   - Success - If user with same email doesn't exist
    
### 2. /login
   POST<br>
   Authenticates the user and returns access token if login is successful.
   <br>
   No Authentication Required 
   <br>
   Arguments:
   - email : String
   - password : String
    
   Returns:
   - access : Access token that the user can use for future requests.
   - refresh : Refresh token that can be used for generating a new Access Token
   
### 3. /movie
   POST<br>
   Adds a new movie.
   <br>
   User Authentication Required 
   <br>
   Arguments:
   - name : String
   
   Returns:
   - Details of the Movie added 
   
   GET<br>
   Returns a list of all movies with movieId, name, and created by.


### 4. /rate
   POST<br>
   Rates the movie
   <br>
   User Authentication Required 
   <br>
   Arguments:
   - rating : Between {1,5}
   - movie_id
   
   Returns:
   - Success - Movie is rated

