-- select name, category from products 
-- where category in ('Shoes', 'Accessories') 

select name, price from products where price BETWEEN 200 AND 550;

select * from products where name like 's%';  -- get everything where name starts from s

select first_name, joined_date from customers
where joined_date >= '2025-01-01';

select name, price from products order by price desc;

select name, price from products order by price desc limit 3;

select distinct city from customers;

select name as products, price as price_sek from products; -- we modify how to displyed values look

select * from customers where city = NULL;
select * from customers where city is null;

-- LAB1

-- 1.1
select first_name, email from customers;

-- 1.2
select * from products where category = 'Shoes';

-- 1.3
select * from customers where city = 'Uppsala';

-- 1.4
select * from products where price = '199';

-- 1.5
select * from products order by name ASC;

-- 1.6
select * from customers order by joined_date;

-- 1.7
select * from products where stock = '0';

-- 1.8
select * from customers order by joined_date DESC;

-- 1.9
select first_name, last_name from customers where city in ('Göteborg', 'Stockholm');

-- 1.10
select name as product, price as price_sek from products order by price;

-- Bonus Questions
-- B.1
select * from products where category in ('Clothing', 'Shoes') AND price > 1000;

-- B.2
select stock, name, price, (stock * price) as stock_value from products 
where stock > 0 order by stock_value DESC;

-- B.3
select * from customers where first_name LIKE '____';

-- B.4
select * from products order by price LIMIT 5 OFFSET 5;

-- B.5
select * from customers where joined_date < '2025-01-01' AND city not in ('Uppsala')
order by city, last_name asc;

-- Extra Challenges
-- Exercise 1
select * from products where category not in ('Accessories') AND stock > 0 AND name like '% %'
order by category, price DESC;

-- Exercise 2
select * from customers where city like 'S%' OR city like 'M%' OR city is NULL;