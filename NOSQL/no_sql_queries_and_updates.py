from datetime import datetime

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

#part1(db)

def part2(db):
    print("\n####################### Exercise 7 #######################\n")

    for row_data in db.orders.find({"items.product_id" : 2}):
        print(row_data["_id"])

    print("\n####################### Exercise 8 #######################\n")
    #for row_data in db.products.find():
    #    print(row_data)
    result = db.products.find({"category" : "Accessories"})
    if result != None:
        db.products.update_many({"category" : "Accessories"}, {"$inc" : {"price" : 20}})

    for row_data in result:
        print(row_data["name"], row_data["category"], row_data["price"])

    print("\n####################### Exercise 9 #######################\n")
    #f
#    db.products.update_many({"name": "Rain Jacket"}, {"$push": {"tags": "new"}, "$set" : {"restock_date" : datetime.now()}})
    db.products.update_many({"name": "Rain Jacket"}, {"$addToSet": {"tags": "new"}, "$set" : {"restock_date" : datetime.now()}})

    for row_data in db.products.find({"name": "Rain Jacket"}):
        print(row_data)

    print("\n####################### Exercise 10 #######################\n")
    print("Show all orders with status new and made before 2026-03-20:\n")
    for all_orders in db.orders.find({"$and": [{"status" : "new"}, {"order_date" : {"$lte" : datetime(2026, 3, 20)}}]}):
        print(all_orders)
    db.orders.delete_many({"$and": [{"status" : "new"}, {"order_date" : {"$lte" : datetime(2026, 3, 20)}}]})

    print("\n\nDELETION COMPLETE.\nShow all orders with status new and made before 2026-03-20:\n")
    if db.orders.count_documents({"$and": [{"status" : "new"}, {"order_date" : {"$lte" : datetime(2026, 3, 20)}}]}) == 0:
        print("\nNo orders with such criteria remain. Orders deleted.")

part2(db)
