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

# Exercise 1
'''
cursor.execute("SELECT first_name, last_name, city from customers")
data_ex_1 = cursor.fetchall()
for name, last, city in data_ex_1:
    print(f"{name} {last} {city}")
'''
# Exercise 2
'''
max_price = float(input("Please provide max price: "))
cursor.execute("SELECT name, category, price, stock from products where price < ?", (max_price,))
data_ex_2 = cursor.fetchall()
for name, category, max_price, stock in data_ex_2:
    print(f"{name} {category} {max_price} {stock}")
'''

# Exercise 3

category = input("Please provide a category. Available categories are: Clothing, Accessories, Shoes.\n").upper()

cursor.execute("SELECT count (*) from products where category = ?", (category,))
print(f"{category} category has {cursor.fetchone()[0]} products")


# Exercise 4




















connection.close()
