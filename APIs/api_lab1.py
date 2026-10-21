import requests, os
from dotenv import load_dotenv, find_dotenv
from api_client import get_json

def part1():
    print("\n############################ Part I Task I ############################\n")
    
    product_data = get_json("https://fakestoreapi.com/products")
    sorted_products = sorted(product_data, key = lambda value: value['price'])
    print(f"{"Title":<52} {"Price":>5}")
    for product in sorted_products[:5]:
        print(f"{product['title']:<52} ${product['price']:>5}")

    """
    print("\n############################ Part I Task II ############################\n")
    
    categories = requests.get("https://fakestoreapi.com/products/categories").json()
    print(categories)
    print("\nPlease type any of the displayed categories to see the products inside:")
    while True:
        user_input = input().lower()
        if user_input in categories:
            fetch_category_data = requests.get(f"https://fakestoreapi.com/products/category/{user_input}").json()
            sorted_products = sorted(fetch_category_data, key = lambda value: value['price'])
            print("The amount of products in the chosen category", user_input, "is", len(fetch_category_data), "and the cheapest product is",
                  sorted_products[0]['title'], "valued at", sorted_products[0]['price'],"$" )
            break
        else:
            print("You did not type any of the correct categories. Try again laddie.")
"""
    print("\n############################ Part I Task IV ############################\n")
    
    new_product = {"title" : "PC",  'price' : 1444, 'description' : 'old cheap PC', 'image' : "let's pretend this is an image", 'category' : 'electronics' }
    response = requests.post("https://fakestoreapi.com/products", json = new_product)
    print("\nStatus code of post operation: ", response.status_code, " and answer is:", response.json())
    product_id = response.json()['id']
    response = requests.patch(f"https://fakestoreapi.com/products/{product_id}", json = {'price' : 1555})
    print("\nStatus code of patch operation:", response.status_code, " and answer is:", response.json())

    print("\n############################ Part I Task V ############################\n")

    get_json("https://httpMadeUpDomainCalledSunnyDay.com", timeout=0.001)

    get_json("https://fakestoreapi.com/status/404")

    get_json("MadeUpDomainCalledSunnyDay.com")

    response = get_json("https://fakestoreapi.com/products", params={"limit" : 5, "sort" : "desc"})
    print(response)


def get_city(user_input):
   
    response = get_json("https://geocoding-api.open-meteo.com/v1/search", params= {"name" : user_input, "count" : 1})
    print(response)
    return response

def get_weather(latitude, longitude):
    response = get_json("https://api.open-meteo.com/v1/forecast", params= {
        "latitude" : latitude,
        "longitude" : longitude,
        "current" : "temperature_2m,wind_speed_10m"})
    print(response)
    return response

def part2():
    
    print("\n############################ Part II Task I, IV ############################\n")
    print("Please providde a city to get its latitude and longitude coordinates:")
    user_input = None
    while True:
        try:
            user_input = input()
            response = get_city(user_input)
            print(response)
            if response:
                print("City: ", user_input, "Latitude", response["results"][0]["latitude"], "Longitude", response["results"][0]['longitude'])
                break
        except KeyError as exception:
            print("We got a key error", exception)
        
    
    print("\n############################ Part II Task II ############################\n")
    print("Printing out the weather data:\n")
    weather = get_weather(response["results"][0]["latitude"], response["results"][0]['longitude'])

    print("\n############################ Part II Task III ############################\n")
    print(f"\nPutting it together:\n{user_input}, {response["results"][0]['country']}:\
          {weather['current']['temperature_2m']}{weather['current_units']['temperature_2m']},\
          wind {weather['current']['wind_speed_10m']} {weather['current_units']['wind_speed_10m']}")


def part3():
    
    print("\n############################ Part III Task I-IV ############################\n")
    load_dotenv(find_dotenv())
    token = os.getenv("GITHUB_TOKEN")
    print(token is None)
    print(find_dotenv())

    print("Please provide a github username to check this users repositories:")
    user_input = input()
    response = requests.get(f"https://api.github.com/users/{user_input}/repos", 
                            params = {"sor" : "pushed", "per_page" : 5},
                            headers ={"Authorization" : f"Bearer {token}"})
    print("Printing response with the bearer token: ", response.headers["X-RateLimit-Limit"])

    tokenless_response = requests.get(f"https://api.github.com/users/{user_input}/repos", 
                            params = {"sor" : "pushed", "per_page" : 5})
    print("Printing response WITHOUT the bearer token: ", tokenless_response.headers["X-RateLimit-Limit"])



if __name__ == '__main__':
    #part1()
    #part2()
    part3()
    