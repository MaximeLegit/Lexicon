import os
from fastapi import FastAPI, HTTPException, Header, Depends
from pydantic import BaseModel
from dotenv import load_dotenv, find_dotenv


# ############################ Part III, Task I ############################

load_dotenv(find_dotenv())
API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise RuntimeError("Missing _API_KEY. Set it in your .env file and try again. Au revoir.")

# ############################ Part III, Task I ############################

app = FastAPI()

@app.get("/")
def home():
    return {"message" : "My First API"}

movies = [
    {"id": 1, "title": "Dune (Part Two)", "director": "Denis Villeneuve", "year": 2024},
    {"id": 2, "title": "Kingdom of Heaven (Director's Cut)", "director": "Ridley Scott", "year": 2005},
    {"id": 3, "title": "The Lord of the Rings The Fellowship of the Ring", "director": "Peter Jackson", "year": 2001},
    {"id": 4, "title": "The Lord of the Rings The Two Towers", "director": "Peter Jackson", "year": 2002}
]


# ############################ Part III, Task III ############################

def check_key(x_api_key : str | None = Header(default=None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401)

# ############################ Part III, Task III ############################


# ############################ Part I, Task I ############################
@app.get("/movies")
def get_movies(director : str | None = None , year : int | None = None):
    output = movies
    if director:
        output = [movie for movie in movies if director in movie["director"]]
    elif year:
        output = [movie for movie in movies if year == movie["year"]]
    if not output:
        raise HTTPException(status_code=404, detail="Requested movie not found.")
    return output

# ############################ Part I, Task II ############################
def find_movie(id: int):
    for movie in movies:
        if movie['id'] == id:
            return movie
    raise HTTPException(status_code=404, detail="Requested movie not found.")

@app.get("/movies/{movie_id}")
def get_movie(movie_id: int):
    return (find_movie(movie_id))
# Status codes: 200 on movie ID 1; 404 on ID 99 ( does not exist ); For 'movie_id': Value must be an integer on 'abc' input


# ############################ Part I, Task III ############################

#get/movies function has been edited.

# ############################ Part I, Task IV ############################

class Movie(BaseModel):
    title : str
    director : str
    year: int

@app.post("/movies", status_code=201, dependencies=[Depends(check_key)])
def add_movie(movie: Movie):

    new_id = max((movie["id"] for movie in movies), default = 0) + 1
    new_movie = {"id" : new_id, "title" : movie.title, "director" : movie.director, "year" : movie.year}
    movies.append(new_movie)

    return new_movie

# As per lecture, it seems pydantic library, after giving it my first input, still understands that even if I submit a year as a string, it is still defined
# as int in the class right. Further, the director, even though it was empty in the 2nd example, it is still an empty string. 

# ############################ Part I, Task V ############################

@app.put("/movies/{movie_id}", dependencies=[Depends(check_key)])
def movie_lookup(movie_id : int, movie : Movie):
    current_movie = get_movie(movie_id)
    current_movie['title'] = movie.title
    current_movie['director'] = movie.director
    current_movie['year'] = movie.year
    return current_movie

@app.delete("/movies/{movie_id}", status_code=204, dependencies=[Depends(check_key)])
def delete_movie(movie_id : int):
    current_movie = get_movie(movie_id)
    movies.remove(current_movie)

# When attempting to delete a movie a second time, we get into the clause of "if not output", menaing, the object we tried to purge is not there,
# hence the exception.


# ############################ Part II, Task I ############################

class MovieUpdate(BaseModel):
    title : str | None = None
    director : str | None = None
    year: int | None = None

@app.patch("/movies/{movie_id}", dependencies=[Depends(check_key)])
def update_movie(movie_id : int, movie_update : MovieUpdate):
    current_movie = find_movie(movie_id)
    current_movie.update(movie_update.model_dump(exclude_unset=True))
    return current_movie

# ############################ Part II, Task II ############################

'''
Response body:
{
  "id": 1,
  "title": "Dune (Part Two)",
  "director": "Denis Villeneuve",
  "year": 2000
}

Response from get movies/movies_id
{
  "id": 1,
  "title": "Dune (Part Two)",
  "director": "Denis Villeneuve",
  "year": 2000
}

# ############################ Part II, Task III ############################

What happenes with an empty body? According to my code, I got same output as above, with exception of year, it is 2024, as my original dictionary. Status code 200.
What happens with a year written as text? I used "2000". It worked due to the pydantic library. When written twothousand, I got a 422 unprocessable error.
Non existing ID? I get the expected error msg the movie is not found, status code 404.

# ############################ Part II, Task IV ############################
In my view, put is not a good practice since it replaces the whole data set it seems. Patch only updates the selected fields, which is more safe. In my practice,
if you want a new row, data etc, first delete it so you know what you are deleting, then insert new data, like via put. It all depends on how person codes and their
viewpoint on data integrity.

'''



# Key generated via python3-64.exe -c "import secrets; print(secrets.token_hex(16))"

# ############################ Part III, Task V ############################

# Without key ? Status code 401, Unauthorised.
# With key, status code 201, year changed.
# Wrong key ? Status code 401, Unauthorised.
