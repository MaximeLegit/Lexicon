from api_client import get_json
import requests

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
