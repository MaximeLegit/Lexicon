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

basics(db)