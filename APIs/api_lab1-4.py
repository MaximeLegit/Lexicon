import requests
from api_client import get_json

def lab1():
    print("\n############################ Task 1 ############################\n")
    
    product_data = get_json("https://fakestoreapi.com/products")
    sorted_products = sorted(product_data, key = lambda value: value['price'])
    print(f"{"Title":<52} {"Price":>5}")
    for product in sorted_products[:5]:
        print(f"{product['title']:<52} ${product['price']:>5}")

    """
    print("\n############################ Task 2 ############################\n")
    
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
    print("\n############################ Task 4 ############################\n")
    
    new_product = {"title" : "PC",  'price' : 1444, 'description' : 'old cheap PC', 'image' : "let's pretend this is an image", 'category' : 'electronics' }
    response = requests.post("https://fakestoreapi.com/products", json = new_product)
    print("\nStatus code of post operation: ", response.status_code, " and answer is:", response.json())
    product_id = response.json()['id']
    response = requests.patch(f"https://fakestoreapi.com/products/{product_id}", json = {'price' : 1555})
    print("\nStatus code of patch operation:", response.status_code, " and answer is:", response.json())

    print("\n############################ Task 5 ############################\n")

    get_json("https://httpMadeUpDomainCalledSunnyDay.com", timeout=0.001)

    get_json("https://fakestoreapi.com/status/404")

    get_json("MadeUpDomainCalledSunnyDay.com")

    response = get_json("https://fakestoreapi.com/products", params={"limit" : 5, "sort" : "desc"})
    print(response)

























if __name__ == '__main__':
    lab1()