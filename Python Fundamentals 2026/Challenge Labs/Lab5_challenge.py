# Part 2 Create Orders

products = [{"Product": "Mango", "Price": 100, "Category": "Fruits"},
            {"Product": "Pineapple", "Price": 200, "Category": "Fruits"},
            {"Product": "Shoes", "Price": 300, "Category": "Outdoor"},
            {"Product": "Fish", "Price": 400, "Category": "Frozen Food"},
            {"Product": "Umbrella", "Price": 500, "Category": "Outdoor"},
            {"Product": "Tea", "Price": 50, "Category": "Broad Food"},
            {"Product": "Coffee", "Price": 250, "Category": "Broad Food"},
            {"Product": "Bike Holder", "Price": 100, "Category": "Instruments"}]

customers = [{"Name" : "Anna", "Email" : "anna@ericsson.com", "Customer ID" : "anneri"},
             {"Name" : "Lena", "Email" : "lena@ericsson.com", "Customer ID" : "leneri"},
             {"Name" : "Anton", "Email" : "anton@ericsson.com", "Customer ID" : "anteri"},
             {"Name" : "Oskar", "Email" : "oskar@ericsson.com", "Customer ID" : "oskeri"},
             {"Name" : "max", "Email" : "max@ericsson.com", "Customer ID" : "maxeri"}]

order = []

def creating_an_order(customer_info, *products, **optional_information):
    total_cost = 0
    order_settings = []
    for product in products:
        total_cost += product["Price"]
        order_settings.append(f"{"Product"} : {product["Product"]}")

    for key, value in optional_information.items():
        if key == "discount" and value == "yes":
            total_cost -= (total_cost * 0.10)

        order_settings.append(f"{key} : {value}")
    order_id = customer_info["Name"] + str(total_cost)
    return {"Customer" : customer_info["Name"], "OrderID" : order_id, "Total cost" : total_cost, "Order settings" : order_settings}

first_order = creating_an_order(customers[0], 
                                    products[0], products[1],
                                    shipping_info = "airplane", discount = "no", priority = "low", gift_message = "Miss you", delivery_instructions = "Hand in Person", campaign_code = "N/A")
second_order = creating_an_order(customers[1], 
                                    products[2], products[3],
                                    shipping_info = "truck", discount = "yes", gift_message = "Miss you", campaign_code = "Happy10")
third_order = creating_an_order(customers[2], 
                                    products[4], products[5],
                                    shipping_info = "ship", discount = "yes", priority = "medium", delivery_instructions = "Leave at apartment", campaign_code = "N/A")
fourth_order = creating_an_order(customers[3], 
                                    products[0], products[5],
                                    shipping_info = "truck", discount = "no", priority = "low", delivery_instructions = "Post Box", campaign_code = "Great#10")
fifth_order = creating_an_order(customers[-1], 
                                    products[-1], products[-2],
                                    shipping_info = "ship", discount = "yes", priority = "high", gift_message = "Happy Birthday")

#print(fourth_order)


# Part 3 Variable Number of products