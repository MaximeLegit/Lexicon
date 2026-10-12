import sqlite3
 
 
def connect():
    conn = sqlite3.connect("webshop.db")
    conn.execute("PRAGMA foreign_keys = ON")
    return conn
 
 
def list_products(conn):
    cursor = conn.execute("SELECT product_id, name, price, stock FROM products")
    for pid, name, price, stock in cursor.fetchall():
        print(f"{pid:>3}  {name:<20} {price:>8.2f} kr  ({stock} in stock)")
 
 
def search_customers(conn):
    city = input("City: ")
    cursor = conn.execute(
        "SELECT first_name, last_name FROM customers WHERE city = ?", (city,))
    rows = cursor.fetchall()
    if not rows:
        print("No customers found.")
    for first, last in rows:
        print(first, last)
 
 
def add_product(conn):
    name = input("Name: ")
    category = input("Category: ")
    price = float(input("Price: "))
    stock = int(input("Stock: "))
    conn.execute(
        "INSERT INTO products (name, category, price, stock) VALUES (?, ?, ?, ?)",
        (name, category, price, stock))
    conn.commit()
    print("Saved!")

def change_stock_of_products(conn):
    product_to_change = int(input("product_to_change ID please: "))
    set_stock_to = int(input("set_stock_to: "))
    conn.execute("update products set stock = ? where product_id = ?", (set_stock_to, product_to_change))

def show_receipt(conn):
    order_id = int(input("Enter order ID: "))
    query = conn.execute("select o.order_id, product.name, oi.unit_price from orders o"
    " join order_items oi on oi.order_id = o.order_id"
    " join products product on product.product_id = oi.product_id where o.order_id = ?", (order_id,))
    print(f"{"order_id":<8} {"product_name":<20} {"unit_price":>8}")
    for o_id, p_name, oi_up in query:
        print(f"{o_id:<8} {p_name:<20} {oi_up:>8.2f}")

def best_sellers(conn):

    query = conn.execute("select name, category, price from products group by category order by price DESC limit 3")
    for name, cat, price in query:
        print(name, cat, price)

def main():
    conn = connect()
    while True:
        print("\n1) List products  2) Search customers  3) Add product 4) Change the stock of a product 5) Show Order Receipt 6) Top 3 Best Selling Products 0) Quit")
        choice = input("> ")
        if choice == "1":
            list_products(conn)
        elif choice == "2":
            search_customers(conn)
        elif choice == "3":
            add_product(conn)
        elif choice == "4":
            change_stock_of_products(conn)
        elif choice == "5":
            show_receipt(conn)
        elif choice == "6":
            best_sellers(conn)
        elif choice == "0":
            break
    conn.close()
 
 
main()
 