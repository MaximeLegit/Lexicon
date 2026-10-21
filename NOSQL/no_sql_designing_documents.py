from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

def ex_one_to_five(db):
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

def ex_six_to_ten(db):
    
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
    result = db.products.aggregate([
        {"$unwind" : "$tags"},
        {"$group" : {"_id" : "$tags", "tag_count" : {"$sum" : 1}}},
        {"$sort" : {"tag_count" : -1 }}
    ])
    for row in result:
        print(row)

if __name__ == '__main__':
    #ex_one_to_five(db)
    ex_six_to_ten(db)
