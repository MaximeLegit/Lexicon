# ==================================================
# TASK 1
# ==================================================

products = [
    {"name": "Laptop", "price": 12000, "stock": 4},
    {"name": "Mouse", "price": 350, "stock": 0},
    {"name": "Keyboard", "price": 800, "stock": 6},
    {"name": "Monitor", "price": 3200, "stock": 3},
    {"name": "Headset", "price": 950, "stock": 0},
    {"name": "Webcam", "price": 1100, "stock": 5}
]

# 1. Loop through the products.
# 2. Print the name of every product that is in stock.
# 3. Calculate the total value of all products in stock.
#    The value of a product is price * stock.
# 4. Print the total value.
# 5. Keep track of which in-stock product has the highest price
#    without using max(), and print its name.


# Write your solution below:
total = 0
current_highest_price = 0
highest_price = []
for product in products:
    if(product["stock"] > 0):
        total += product["stock"] * product["price"]
        if (current_highest_price < product["price"]):
            highest_price = {product["name"] : product["price"]}
            current_highest_price = product["price"]
        print("Products in stock are:", product["name"])

print("Total value of all products in stock:", total, "Highest price item:", highest_price)



# ==================================================
# TASK 2
# ==================================================

scores = [78, 92, 55, 81, 67, 95, 73]

# Create a function called calculate_average that:
# - receives a list of scores
# - calculates and returns the average score
#
# Create another function called create_result that:
# - receives a list of scores
# - uses calculate_average()
# - returns "PASS" if the average is 70 or higher
# - otherwise returns "FAIL"
#
# Call create_result() using the scores above.
# Print both the average score and the final result.


# Write your solution below:

def calculate_average(scores):
    return sum(scores) / len(scores)
average_value = calculate_average(scores)
print(average_value)

def create_result(scores):
    average_value = calculate_average(scores)
    if average_value >= 70:
        return "PASS"
    else:
        return "FAIL"
result_value = create_result(scores)
print(f"Average score: {round(average_value,2)}, Final Result: {result_value}")
    
# ==================================================
# TASK 3
# ==================================================

product_prices = [250, 400, 150, 700]

order_settings = {
    "discount": 10,
    "shipping": 49,
    "priority": True
}

# Create a function called calculate_order that:
# - receives a customer name as a normal parameter
# - receives any number of product prices using *args
# - receives optional settings using **kwargs
# - calculates the subtotal of all product prices
# - applies the discount percentage if "discount" exists
# - adds shipping if "shipping" exists
# - returns a dictionary containing:
#       customer
#       subtotal
#       final_total
#       settings
#
# Call the function using:
# - customer name "Anna"
# - the values from product_prices using unpacking
# - the values from order_settings using dictionary unpacking
#
# Print the returned dictionary.


# Write your solution below:

def calculate_order(name, *prices, **order_settings):
    prices_subtotal = 0
    final_total = 0
    for price in prices:
        prices_subtotal += price
    for key, value in order_settings.items():
        if key == "discount":
            discount = (prices_subtotal * (value / 100))
            final_total = prices_subtotal - discount + order_settings["shipping"]
            break
        else:
            final_total = prices_subtotal + order_settings["shipping"]

    return {"Customer:" : name, "prices_subtotal:" : prices_subtotal, "final_total:" : final_total, "settings:" : order_settings}
result = calculate_order("Anna", *product_prices, **order_settings)
print("Show me:", result)

# ==================================================
# TASK 4
# ==================================================

players = [
    {"name": "  anna", "score": 85, "active": True},
    {"name": "DAVID ", "score": 72, "active": False},
    {"name": " sara ", "score": 94, "active": True},
    {"name": "LEO", "score": 67, "active": True},
    {"name": " emma", "score": 88, "active": True},
    {"name": "OSCAR ", "score": 76, "active": False}
]

# 1. Create a new list containing normalized player names.
#    Remove unnecessary whitespace and use consistent capitalization.
#    Use a list comprehension.
#
# 2. Create a new list containing only the active players
#    with a score of 80 or higher.
#    Use a list comprehension.
#
# 3. Sort the original players by score from highest to lowest.
#    Use sorted() with a lambda.
#
# 4. Print the ranking in the following format:
#
#    1. Sara - 94
#    2. Emma - 88
#    ...
#
#    Generate the ranking numbers using enumerate().
#
# 5. Create a separate list containing the player names and
#    another list containing their scores.
#    Combine them using zip() and print each name together
#    with its score.


# Write your solution below:
normalised_players = [player["name"].strip().title() for player in players]
print(normalised_players)

active_players = [player["name"].strip().title() for player in players if player["active"]]
print(active_players)

sorted_players = sorted(players, key = lambda value: value["score"])
print(sorted_players)

reversed_sorted_players = sorted(players, key = lambda value: value["score"], reverse=True)
for index, player in enumerate(reversed_sorted_players):
    print(f"{index}. {player["name"].strip().title()} - {player["score"]}")

only_player_names = [player["name"].strip().title() for player in players]
only_their_score = [player["score"] for player in players]

print("Part 5:\n")
for name, score in zip(only_player_names, only_their_score):
    print(name, score)