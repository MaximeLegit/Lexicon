import requests
import os
from dotenv import load_dotenv

def tresting():
    response = requests.get("https://fakestoreapi.com/products").json()
    print(response, "\n",response.status_code, "\n",response.headers["Content-Type"])
    print(response.text[:200])
    #print(response.text[0]['title'])
    data = response.json()
    #print(type(data))
    #print(len(data))
    #print(data[0])
    for product in data[:5]:
        print(f"{product['id']} : {product['title']} - ${product['price']}")
    print(product['rating']['rate'])
    print(product['rating']['rate'])


def some_more():
    response = requests.get("https://fakestoreapi.com/products", params={"limit" : 5, "sort" : "desc"})
    print(len(response.json()))
    print(response.url)
    print([product['id'] for product in response.json()])


def and_then_some():
    try:
        response = requests.get("https://api.github.com/users/this-user-does-not-exist-1234")
        response.raise_for_status()
        print(response.json()['name'])
    except requests.exceptions.HTTPError as error:
        print(f"The errir: {error.response.status_code}")

def get_json(url, params=None, headers=None, timeout=5):
    try:
        response = requests.get(url, params=params, headers=headers, timeout=timeout)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        print("The requesst took too long")
    except requests.exceptions.ConnectionError:
        print("Could not connect to the server")
    except requests.exceptions.HTTPError as error:
        print(f"The server said no: {error.response.status_code}")
    except requests.exceptions.JSONDecodeError:
        print("The answer was not JSON")
    except requests.exceptions.RequestException as error:
        print(f"Someting else went wrong: {type(error).__name__}")
    return None

def modifying_data():
    new_product = {"title" : "bobb",  'price' : 14.5, 'description' : 'something magical', 'category' : 'electronics' }
    response = requests.post("https://fakestoreapi.com/products", json = new_product)
    print(response.status_code)
    print(response.json())
    print(response.request.headers['Content-Type'])
    print(response.request.body)

    #response = requests.post("https://fakestoreapi.com/products", data = new_product)

def put_replacing_data():
    updated_product = {"title" : "ghost",  'price' : 177.5, 'description' : 'something ghastly', 'category' : 'electronics' }
    response = requests.put("https://fakestoreapi.com/products/7", json = updated_product)
    print(response.status_code)
    print(response.json())

def patch_example():
    response = requests.patch("https://fakestoreapi.com/products/7", json = {'price' : 222})
    print(response.status_code)
    print(response.json())

def delete():
    response = requests.delete("https://fakestoreapi.com/products/6")
    print(response.status_code)
    print(response.json())

def last_part():
    response = requests.get("https://api.github.com/users/octocat")
    print(response.headers["X-RateLimit-Limit"])
    print(response.headers["X-RateLimit-Remaining"])

def token_emphasis():
    # create a file .env
    # GITHUB_TOKEN = GHP
    load_dotenv()
    token = os.getenv("GITHUB_TOKEN")
    headers = {"Authorization" : f"Bearer {token}"}
    response = requests.get("https://api.github.com/user", headers = headers)
    print(response.status_code)

if __name__ == '__main__':
    #patch_example()
    delete()
    last_part()