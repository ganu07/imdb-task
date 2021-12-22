# python_project_imdb

The imdb api application starts with basic auth with username = admin and password = admin

use Postman API to send the request : https://web.postman.co/

The api start with this = GET https://flask-imd.herokuapp.com/

1) GET all the search movie with this request 
   GET https://flask-imd.herokuapp.com/v1/movies
   The result will appear all the movies from database
    
    For the view movie no need to auth but while updating, deleting and adding movie need admin auth.

    If you want perticular search movie then use the request like this: 
     GET https://flask-imd.herokuapp.com/v1/movies?name=star
         
    {
       "total": 2,
       "data": [
           {
               "id": 2,
               "99popularity": 88.0,
               "director": "George Lucas",
               "genre": [
                   "Action",
                   "Adventure",
                   "Fantasy",
                   "Sci-Fi"
               ],
               "imdb_score": 8.8,
               "name": "Star Wars"
           },
           {
               "id": 7,
               "99popularity": 86.0,
               "director": "Marc Daniels",
               "genre": [
                   "Adventure",
                   "Sci-Fi"
               ],
               "imdb_score": 8.6,
               "name": "Star Trek"
           },
    }
 
 
2) A POST API for adding new movies accepts json input. ALL Fields Mandatory
   POST https://flask-imd.herokuapp.com/v1/movies
    
    {
    "99popularity": 83.0,
    "director": "Victor Fleming",
    "genre": [
      "Adventure",
      " Family",
      " Fantasy",
      " Musical"
    ],
    "imdb_score": 8.3,
    "name": "The Wizard of Oz"
    }


3) A PUT API to edit existing movie details. Accepts id in param and all the edit fields in body.
    Request:
    PUT https://flask-imd.herokuapp.com/v1/movies?id=2&popularity=83.0
    :param id: Required

    Request Body: - Any one of the field given below is required
    {
    "99popularity": 83.0,
    "director": "Victor Fleming",
    "genre": [
      "Adventure",
      " Family",
      " Fantasy",
      " Musical"
    ],
    "imdb_score": 8.3,
    "name": "The Wizard of Oz"
    
    
 4. A DELETE API to delete movies stored in db based on the id passed in param
    Request:
    DELETE https://flask-imd.herokuapp.com/v1/movies?id=1
    :param id: Required
    }
