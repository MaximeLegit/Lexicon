from api_client import get_json
import requests

BASE = "http://127.0.0.1:8000"

books = get_json(f"{BASE}/books")
print(books)

new_book = {"title" : "Snow Crash", "author" : "Neak Stephenson", "year" : 1992}
response = requests.post(f"{BASE}/books", json = new_book, timeout = 2)

get_json(f"{BASE}/books/99")