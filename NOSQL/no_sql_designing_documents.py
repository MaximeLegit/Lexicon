from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

def ex_one_to_five(db):
    print("\n####################### Exercise 1 #######################\n")
    print("Reference reviews. Why? It is my understanding that reviews can spawn over time, over many years. This list grows." \
    "\nPeople ofthen edit their reviews. Suffice to say, it is subject to change. Hence, not constant -> reference.")

    print("\Reference members. Why? It depends here but referencing members is safer since members can be few, but can be many also." \
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


if __name__ == '__main__':
    ex_one_to_five(db)