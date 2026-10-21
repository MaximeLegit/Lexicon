import json

from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError


client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

secondary_client = MongoClient("mongodb://localhost:27018/", serverSelectionTimeoutMS=2000)
scnd_db = secondary_client["webshop"]

def ex_one_to_five():
    print("\n####################### Exercise 1 #######################\n")
    print("Reference reviews. Why? It is my understanding that reviews can spawn over time, over many years. This list grows." \
    "\nPeople ofthen edit their reviews. Suffice to say, it is subject to change. Hence, not constant -> reference.")

    print("\nReference members. Why? It depends here but referencing members is safer since members can be few, but can be many also." \
    "\nPeople can become members, they can also stop being members. This data is also subjected to change, hence -> reference")

    print("\n####################### Exercise 2 #######################\n")
    print("Copying data is fast, hence it is convenient to use, on small data sets particularly. However, as pointed out in the lecture" \
    "\nwe can have thousands of orders, say amazon. If you change the name of the product, you would need to update those thousand of orders as well. Inte bra.")

    print("\n####################### Exercise 3 #######################\n")
    db.newsletter_signups.drop()
    db.create_collection("newsletter_signups", validator = { 
        "$jsonSchema" : {"required" : ["email", "source"], 
                         "properties" : {
                             "email" : {"bsonType" : "string"}, 
                             "source" : {"enum" : ["web", "store"]}}
                        }
    })
    db.newsletter_signups.insert_one({"email" : "lola@example.com", "source" : "web"})
    #db.newsletter_signups.insert_one({"email" : "max@example.com", "source" : "store"}) <- as expected
    db.newsletter_signups.drop()

    print("\n####################### Exercise 4 #######################\n")

    result = db.customers.aggregate([
        {"$match" : {"city" : { "$in" : ["Göteborg", "Stockholm", "Uppsala" ]}}},
        {"$group" : {"_id" :"$city", "count" : {"$sum" : 1}}},
        {"$sort" : {"count" : -1}}
    ])
    for row in result:
        print(row)

    print("\n####################### Exercise 5 #######################\n")
    result = db.products.aggregate([
        {"$match" : {"category" : { "$in" : ["Clothing", "Accessories", "Shoes" ]}}},
        {"$sort" : {"price" : 1 }},
        {"$group" : {"_id" : "$category", "cheapest_product" : {"$first" : "$name"}, "cheapest price" : {"$min" : "$price"}, 
                     "highest expensive" : {"$last" : "$name"}, "this price" : {"$max" : "$price"}}}
    ])
    for row in result:
        print(row)

def ex_six_to_ten():
    
    print("\n####################### Exercise 6 #######################\n")
    
    result = db.orders.aggregate([
        {"$group" : {"_id" : "$customer_id", "nr_of_orders" : {"$sum" : 1}}},
        {"$sort" : {"nr_of_orders" : 1 }},
        {"$match" : {"nr_of_orders" : {"$gte" : 2}}}
        ])
    for row in result:
            print(row)

    print("\n####################### Exercise 7 #######################\n")

    result = db.orders.aggregate([
        {"$project" : {"nr_of_items" : {"$size" : "$items"}}}
    ])
    for row in result:
        print(row)

    print("\n####################### Exercise 8 #######################\n")

    result = db.orders.aggregate([
        {"$match" : {"status" : { "$in" : ["delivered", "shipped", "new"]}}},
        {"$unwind" : "$items"},
        {"$lookup": {
        "from": "products",
        "localField": "items.product_id", # field in orders
        "foreignField": "_id", # field in products
        "as": "output"
        }},
        {"$group" : {"_id" : "$output.category", "Units Sold:" : {"$sum" : "$items.quantity"}}}
    ])
    for row in result:
        print(row)

    print("\n####################### Exercise 9 #######################\n")

    result = db.orders.aggregate([
        {"$match" : {"status" : { "$in" : ["new", "shipped", "delivered", "cancelled"]}}},
        {"$unwind" : "$items"},
        {"$group" : {"_id" : "$status", "total" : {"$sum": {"$multiply" : ["$items.quantity", "$items.unit_price"]}}}}
        ])
    for row in result:
        print(row)

    print("\n####################### Exercise 10 #######################\n")
    result = db.products.find([
        {"$unwind" : "$tags"},
        {"$group" : {"_id" : "$tags", "tag_count" : {"$sum" : 1}}},
        {"$sort" : {"tag_count" : -1 }}
    ])
    for row in result:
        print(row)


def find_orders(request_text):
    data = json.loads(request_text)
    status = data["status"]
    if status not in ["new", "shipped", "delivered", "cancelled"]:
        raise ValueError("Not a valid status. You get 0.")
    return list(db.orders.find({"status": status}))
    # The issue here is that this puts our code open for injections by hackers, by having the query operate directly on the status like that. The better approach here is to remove the status part out of the find operation and check it separately.
    # It is neat and all, and I would have probably written code like this myself, but nowadays, code security and code obfuscation is essential.

def products_under(price):
    result = db.products.find({"price" : {"$lt" : price}})
    return result

def final_stretch():

    user_input = None
    while True:
        print("Please enter a number to get corresponding products under your sum: ")
        try:
            user_input = float(input())
            if isinstance(user_input, float):
                result = products_under(user_input)
                print("\nProducts that cost less than 300 are:\n")
                print(f"{"Name":<15} {"Price":>5}")
                for row_data in result:
                    print(f"{row_data["name"]:<15} {row_data["price"]:>3}")
                break
        except ValueError:
            print("\nPlease enter a number!")
            return []

def exercise_thirteen(database):
    try:
        return database.products.count_documents({})
    except ServerSelectionTimeoutError:
        print("Friendly message.")

def exercise_fourteen():
    print("\n\nQ1. Personal data in customers is first, last name, phone and email. However, city, in my view, can also be considered as personal."
    "\nQ2. This is a good idea if a customer is to be removed, you can easily pattern match on the ID only, no need to cross check several fields and update several places."
    "\nQ3. If the database is small, say 10 people, it may not be bad. Here, the best practice would be to consider scaling and updates. Say you have eventually, like amazon,"
    "\n customers in the thousands/millions. One, the size will be huge, two, updates will be slow, three, not certain this will work actually, if DB can support such size.")

if __name__ == '__main__':
    #ex_one_to_five()
    #ex_six_to_ten()
    #print("\n####################### Exercise 12 #######################\n")
    #final_stretch()
    print("\n####################### Exercise 10 #######################\n")
    
    print("Calling improved find_orders() function with {\"status\": \"new\"} gives us:\n")
    x = find_orders('{"status": "new"}')
    for i in x:
        print(i)

    print("\nCalling improved find_orders() function with {\"$ne\": \"x\"} gives us:\n")
    x = find_orders('{"status": {"$ne": "x"}}')
    for i in x:
        print(i)

    print("\n####################### Exercise 13 #######################\n")
    print("Total amount of products via scnd_db is: ", exercise_thirteen(scnd_db))

    print("Total amount of products via working db is: ", exercise_thirteen(db))
