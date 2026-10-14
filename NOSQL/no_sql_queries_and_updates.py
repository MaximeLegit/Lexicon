from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]


def part1(db):
    print("\n####################### Exercise 1 #######################\n")

    for row_data in db.products.find({"price" : {"$gt" : 1000} }):
        print(row_data["name"], row_data["price"])

    print("\n####################### Exercise 2 #######################\n")

    for row_data in db.orders.find({"status" : {"$ne" : "delivered"} }):
        print(row_data["_id"], row_data["status"])

    print("\n####################### Exercise 3 #######################\n")

    print("\nCustomers who live in Malmö or Stockholm are:\n")
    for row_data in db.customers.find({"city" : {"$in" : ["Malmö", "Stockholm"]} }):
        print(row_data["first_name"], row_data["last_name"])

    print("\n####################### Exercise 4 #######################\n")

    print("\nProducts that are of white colour:\n")
    for row_data in db.products.find({"details.color" : "white"}):
        print(row_data["name"])

    print("\n####################### Exercise 5 #######################\n")

    print("\nProducts that have a sport tag are:\n")
    for row_data in db.products.find({"tags" : "sport"}):
        print(row_data["name"])

    print("\n####################### Exercise 6 #######################\n")

    print("\n5 cheapest products are:\n")
    for row_data in  db.products.find().sort("price", 1).limit(5):
        print(row_data["name"], row_data["price"])

part1(db)
