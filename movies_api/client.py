from api_client import get_json
from main import add_movie
from dotenv import load_dotenv, find_dotenv
import requests, os


BASE = "http://127.0.0.1:8000"

# ############################ Part I, Task VI ############################

list_of_movies = get_json(f"{BASE}/movies")
for m in list_of_movies:
    print(m)

new_movie = {"title" : "The Big Short", "director" : "Adam McKay", "year" : 2015}
response = requests.post(f"{BASE}/movies", json = new_movie, timeout = 2)

print("\nResponse for adding a new movie , via post command, should be:....", response.status_code)

print("\nResponse for the missing movie should be:....\n")
get_json(f"{BASE}/movies/99")


# ############################ Part III, Task VI ############################

movie_spotlight = {"title": "Spotlight", "director": "Tom McCarthy", "year": 2015}
movie_departed = {"title": "The Departed", "director": "Martin Scorsese", "year": 2006}

def add_movie_client_style(movie, api_key = None):
    
    headers = {"X-API-Key": api_key} if api_key else []

    print("\nPart III, Task VI")
    response = requests.post(f"{BASE}/movies", json = movie, timeout = 2, headers=headers)

    return response

load_dotenv(find_dotenv())
api_key = os.getenv("API_KEY")

response = add_movie_client_style(movie_spotlight, api_key)
print("\nTrying post with the key. Result:", response.status_code)

response = add_movie_client_style(movie_departed)
print("\nTrying post WITHOUT the key. Result:", response.status_code)

print("\nPart III, Task VII")
print("\nConfirmed, git status does not show .env file since it is in my .gitignore file. We are safe.")