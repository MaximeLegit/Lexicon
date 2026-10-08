-- ##################  Lecture  ################## 

select * from orders;

select orders.order_id, customers.first_name, orders.order_date from orders 
join customers on orders.customer_id = customers.customer_id;

-- Aliases

select o.order_id, c.first_name, o.order_date from orders o join customers c on o.customer_id = c.customer_id;

select o.order_id, c.first_name, c.city from orders o join customers c on o.customer_id = c.customer_id where c.city = 'Uppsala';

select c.first_name, o.order_date, p.name, oi.quantity
from order_items oi 
join orders o on oi.order_id = o.order_id
join customers c on o.customer_id = c.customer_id
join products p on oi.product_id = p.product_id;

-- er diagram
-- customers <-- orders <-- order_items --> products

select c.first_name, o.order_id from customers c 
left join orders o on c.customer_id = o.customer_id;

-- Does not include joining if result is NULL
select c.first_name, o.order_id from customers c
join orders o on c.customer_id = o.customer_id;

-- ##################  Lecture  ################## 

-- ##################  Exercises  ################## 

select count(*) from orders;

-- Exercise 1

select customer.first_name, customer.last_name, orders.status
from orders join customers customer on customer.customer_id = orders.order_id; 

-- Exercise 2

select customer.first_name, orders.order_id from orders
join customers customer on customer.customer_id = orders.customer_id where customer.first_name = 'Erik';

-- Exercise 3

select customer.first_name, customer.city as 'customer location', orders.order_id from orders
join customers customer on customer.customer_id = orders.customer_id where customer.city = 'Göteborg';

-- Exercise 4

select order_items.order_id, product.name, product.category from order_items
join products product on product.product_id = order_items.product_id;

-- Exercise 5

select order_items.order_id, product.name from order_items
join products product on product.product_id = order_items.product_id where product.category = 'Shoes';

-- Exercise 6

select products.name, oi.quantity, oi.unit_price, oi.quantity * oi.unit_price as 'line total' from products
join order_items oi on oi.product_id = products.product_id where oi.order_id = 10;

-- Exercise 7

select customer.first_name, orders.order_date from orders
join customers customer on customer.customer_id = orders.customer_id
join order_items oi on oi.order_id = orders.order_id
join products product on product.product_id = oi.product_id where product.name = 'Hoodie Black';

-- Exercise 8

select customer.first_name, o.order_id from customers customer 
left join orders o on customer.customer_id = o.customer_id;

-- Exercise 9

select concat(products.name, ' has never been sold') as 'Result:' from products
left join order_items on products.product_id = order_items.product_id where order_items.product_id is NULL;
