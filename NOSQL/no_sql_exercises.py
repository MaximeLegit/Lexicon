from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

# print(client.list_database_names())

def basics(db):
    print("\n####################### Exercise 1 #######################\n")

    for row_data in db.products.find({"category" : "Accessories"}):
        print(row_data["name"])

    print("\n####################### Exercise 2 #######################\n")

    for row_data in db.customers.find({"city" : "Göteborg"}):
        print(row_data["first_name"], row_data["last_name"])

    print("\n####################### Exercise 3 #######################\n")

    print(f"\n{"Product Name":<16} {"Price":>5}\n")
    for row_data in db.products.find():
        print(f"{row_data["name"]:<16} {row_data["price"]:>5}")

    print("\n####################### Exercise 4 #######################\n")

    print("How many customers live in Uppsala?", db.customers.count_documents({"city" : "Uppsala"}))

    print("\n####################### Exercise 5 #######################\n")

    extracted_data = db.products.find_one({"name" : "Sandals"})
    print("How many sandals do we have in stock?", extracted_data.get("stock"))

#basics(db)

def basics_part2(db):

    print("\n####################### Exercise 6 #######################\n")
    
    for row_data in db.customers.find({"newsletter" : True}):
        print(row_data["first_name"], "has gotten a newsletter")

    print("\n####################### Exercise 7 #######################\n")

    insertion = db.customers.insert_one({"first_name": "Maxime", "last_name": "Red Right Hand", 
                                        "city": "Göteborg", "joined": "2026-09-01", "phone": "076-7778899"})
    print("Auto generated ID is: ", insertion.inserted_id)

    finding_myself = db.customers.find_one({"first_name" : "Maxime"})

    db.customers.update_one(finding_myself, {"$set": { 'email': "maxime@email.com" }})
    row_data = db.customers.find_one({"first_name" : "Maxime"})
    if row_data:
        print(row_data)
    else:
        print("Maxime missing")

    print("\n####################### Exercise 8 #######################\n")
    
    products = [
    {"_id": 13, "name": "Gino Green Global", "category": "Clothing", "price": 599, "stock": 15, "tags": ["shiny", "hand-was", "expensive"]},
    {"_id": 14, "name": "Super Mario", "category": "Toy", "price": 249, "stock": 25, "tags": ["toy", "super", "fantastic"]}
    ]
    db.products.insert_many(products)
    print("The amount of products we have is: ", db.products.count_documents({}))

basics_part2(db)
