-- ##################  Lecture  ################## 

insert into orders(order_id, customer_id, order_date, status)
values (222, 1, '2026-10-08', 'delivered');

select * from orders;

insert into order_items(order_id, product_id, quantity, unit_price)
values (1, 1, 1, 539), (2, 2, 2, 777);

select * from orders;

select count (*) from orders;

insert into orders (order_id, customer_id, order_date)
values (34, 7, '2026-10-10');
select * from orders;

update products set price = price * 0.9 where category = 'Shoes';
select name, price from products where category ='Shoes';

select * from customers where customer_id = 9;
delete from customers where customer_id = 9;

-- Relationships and diagrams


CREATE TABLE order_sheet (
  order_no INTEGER,
  customer TEXT,
  email    TEXT,
  city     TEXT,
  products TEXT,
  total    REAL
);
INSERT INTO order_sheet VALUES
(1, 'Anna Lindqvist', 'anna.lindqvist@example.com', 'Uppsala', 'Hoodie Black, Cap Logo x2', 997),
(3, 'Anna Lindqvist', 'anna.lindqvist@example.com', 'Uppsala', 'Socks 3-pack x3', 387),
(4, 'Sara Ahmed', 'sara.ahmed@example.com', 'Goteborg', 'T-shirt White x2, Joggers Grey', 997),
(6, 'Maria Nilsson', 'maria.n@example.com', 'Malmö', 'Hoodie Black, Beanie', 778),
(11, 'Anna Lindqvist', 'anna.l@example.com', 'Uppsala', 'Joggers Grey x2', 998);
 
select * from order_sheet;

select distinct email from order_sheet where customer = 'Anna Lindqvist';

update order_sheet set city = 'Stockholm' where customer = 'Anna Lindqvist';

--Description: A library lends books to members. A member can barrow many books
--A book can be borrowed many times, but only by one member at a time.
--We want to know when a book was borrowed and when it was returned.
 
-- members 1---N loans N---1 books
 
-- ##################  Lecture  ################## 

-- ##################  Lab 3  ################## 

select count(*) from orders;
select * from customers;

-- Exercise 1

insert into customers(customer_id, first_name, last_name, email, city, joined_date)
values (11, 'Lola', 'Mörk', 'lola@amazing.com', 'Gäteborg', '2026-01-01');
select * from customers;

-- Exercise 2

insert into products(product_id, name, category, price, stock)
values (13, 'Scarf', 'Accessories', 229, 15), (14, 'Gloves','Accessories', 199, 20 );
select * from products;

-- Exercise 3

insert into orders(order_id, customer_id, order_date, status)
values (16, 7, '2026-10-07', 'new');
insert into order_sheet values (16, 'Emma Karlsson', 'emma.k@example.com', 'Västerås', '2 Beanies', 358);
select * from orders;
select * from order_sheet;

-- Exercise 4

select * from order_items;
insert into order_items values(16, 16, 0, 345);
-- we shall faill here since the origina constaint in the databe for quantity is more than 0.

-- Exercise 5

update orders set status = 'shipped' where order_id = 12;
select * from orders;

-- Exercise 6

update products set stock = 50 where product_id = 5;
select * from products;

-- Exercise 7

update products set price = price + price * 0.1 where category = 'Accessories';
select * from products;

-- Exercise 8

delete from order_items where order_id in (select order_id from orders where status = 'cancelled');
delete from orders where status = 'cancelled';
select * from orders;
-- I think this is because of the dependency on the foreign key, meaning if you delete the sub table, you need to delete the parent table,
-- roughly like child/parent process I think.

-- Exercise 9

-- Check indeed. The easier way is to just run webshop_reset.sql, to be super safe. Which I have done.