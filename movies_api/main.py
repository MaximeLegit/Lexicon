from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

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

# ############################ Task 1 ############################
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

# ############################ Task 2 ############################
def find_movie(id: int):
    for movie in movies:
        if movie['id'] == id:
            return movie
    raise HTTPException(status_code=404, detail="Requested movie not found.")

@app.get("/movies/{movie_id}")
def get_movie(movie_id: int):
    return (find_movie(movie_id))
# Status codes: 200 on movie ID 1; 404 on ID 99 ( does not exist ); For 'movie_id': Value must be an integer on 'abc' input


# ############################ Task 3 ############################

#get/movies function has been edited.

# ############################ Task 4 ############################

class Movie(BaseModel):
    title : str
    director : str
    year: int

@app.post("/movies", status_code=201)
def add_movie(movie: Movie):
    new_id = max((movie["id"] for movie in movies), default = 0) + 1
    new_movie = {"id" : new_id, "title" : movie.title, "director" : movie.director, "year" : movie.year}
    movies.append(new_movie)
    return new_movie

# As per lecture, it seems pydantic library, after giving it my first input, still understands that even if I submit a year as a string, it is still defined
# as int in the class right. Further, the director, even though it was empty in the 2nd example, it is still an empty string. 

# ############################ Task 5 ############################

@app.put("/movies/{movie_id}")
def movie_lookup(movie_id : int, movie : Movie):
    current_movie = get_movie(movie_id)
    current_movie['title'] = movie.title
    current_movie['director'] = movie.director
    current_movie['year'] = movie.year
    return current_movie

@app.delete("/movies/{movie_id}", status_code=204)
def delete_movie(movie_id : int):
    current_movie = get_movie(movie_id)
    movies.remove(current_movie)

# When attempting to delete a movie a second time, we get into the clause of "if not output", menaing, the object we tried to purge is not there,
# hence the exception.