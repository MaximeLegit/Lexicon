##############  Lecture  ############## 

import sqlite3
connection = sqlite3.connect("webshop.db")
cursor = connection.cursor()

#cursor.execute("SELECT name, price from products order by price DESC")
#rows = cursor.fetchall()

# < is left aligned, > is right aligned, how many spaces etc.
#for name, price in rows:
#    print(f"{name:<20} {price:>8.2f} kr")


# cursor.fetchone()[0]

#city = 'Uppsala'
#cursor.execute("SELECT name, price from products where city = ?", (city,))

##############  Lecture  ############## 


##############  Exercises  ##############

# Exercise 1 - 5

def ex1_5(cursor):
    cursor.execute("SELECT first_name, last_name, city from customers")
    data_ex_1 = cursor.fetchall()
    for name, last, city in data_ex_1:
        print(f"{name} {last} {city}")

    # Exercise 2

    max_price = float(input("Please provide max price: "))
    cursor.execute("SELECT name, category, price, stock from products where price < ?", (max_price,))
    data_ex_2 = cursor.fetchall()
    for name, category, max_price, stock in data_ex_2:
        print(f"{name} {category} {max_price} {stock}")

    # Exercise 3

    category = input("Please provide a category. Available categories are: Clothing, Accessories, Shoes.\n").upper()

    cursor.execute("SELECT count (*) from products where category = ?", (category,))
    print(f"{category} category has {cursor.fetchone()[0]} products")


    # Exercise 4

    # It is dangerous due to possibilities of prompt based insertions/outputs to identify the code and reverse
    # engineer it. This is a, or used to be, a common practice amongst hackers if countermeasures are not taken,
    # suych as limit the amount of logins for example, or the amount of queries that are allowed to be performed.
    # by using ? we give our databse the possibility to pattern match the input without giving away any vital information.

    # Exercise 5-6

    # Code has been added in read.py

# Exercise 7

# The program will crash since we provide string input to an input that expect a float explicitly. There is no try catch for this
# so cras is inevitable.


def ex9_10(cursor):
    
    # Exercise 9

    data_ex_9 = cursor.execute("select product.name, oi.quantity, oi.quantity * oi.unit_price as total_price from orders o"
    " join customers customer on customer.customer_id = o.customer_id"
    " join order_items oi on oi.order_id = o.order_id"
    " join products product on product.product_id = oi.product_id where customer.customer_id = 1")

    print(f"Here are the products you have bought Anna:\n{"Name":<15} {"Quantity":<5} {"Total_price":>8}\n")
    for name, quantity, total_price in data_ex_9:
        print(f"{name:<15} {quantity:<5} {total_price:>9.2f}")

    # Exercise 10

    cursor.execute("update customers set email = 'erik.johansson@example.com' where customer_id = 2")
    cursor.execute("select * from customers where customer_id = 2")
    data_ex_10 = cursor.fetchone()
    print(data_ex_10)

# Exercise 11

def customer_overview(cursor):
    cursor.execute("create view if not exists customers_overview as select customer.customer_id, customer.first_name, customer.city, count(o.order_id) as nr_of_orders" \
    " from customers customer" \
    " left join orders o on o.customer_id = customer.customer_id group by customer.customer_id")
    cursor.execute("select * from customers_overview")
    data_ex_11 = cursor.fetchall()
    print(f"\n{"Customer ID":<11} {"Name":<10} {"City":<10} {"Nr of Orders":>3}\n")

    for id, name, city, o_id in data_ex_11:
        print(f"{id:<11} {name:<10} {city or 'NULL':<10} {o_id:>3}")


customer_overview(cursor)



connection.close()
