-- ##############  Lecture  ############## 


create Table pets (
	pet_id 	INTEGER Primary Key,
	name 	Text,
	species Text,
	age 	Integer
 );

insert into pets VALUES (1, 'Lola', 'Human', 29);
select * from pets;

alter table pets add column owner text;
select * from pets;

drop table pets;

create table pets(
	pet_id  integer primary KEY,
	name	text NOT NULL,
	species text NOT NULL,
	age 	integer check (age >0),
	vaccinated integer default 0
);
drop table pets;

drop table orders;

create table orders(
	order_id  integer primary KEY,
	customer_id	text NOT NULL,
	order_date text NOT NULL,
	status 	text not null default 'new'
		check (status IN ('new', 'shipped', 'delivered', 'cancelled')),
	foreign key (customer_id) references customers(customer_id)
);

drop table order_items;

create table order_items(
	order_id  integer primary KEY,
	product_id	integer NOT NULL,
	order_date integer NOT NULL,
	primary key (order_id, product_id),
	foreign key (order_id) references orders(order_id),
	foreign key (product_id) references products(product_id)
);

drop table order_items;
-- ##############  Lecture  ##############

-- ##############  Day 2  ##############

-- Exercise 1

create table books(
	book_id  	integer primary KEY,
	title	 	text NOT NULL,
	author 		text,
	year		integer not null check (year > 0) -- not accounting for BCE here
)

-- Exercise 2

-- drop table books;
create table books(
	book_id  	integer primary KEY,
	title	 	text NOT NULL,
	author 		text,
	year		integer not null check (year > 1400)
);

-- Exercise 3

alter table books add column isbn text;

-- Exercise 4

drop table books;

-- Exercise 5

drop table reviews;
create table reviews(
	review_id  	integer primary KEY,
	product_id	integer,
	rating		integer check (rating > 0 and rating < 6),
	comment 	text,
	foreign key (product_id) references products(product_id)
);
insert into products values (13, 'Hyperion', 'Book', 199, 2);
insert into reviews VALUES (1, 13, 4, 'Data Science');
select * from reviews;
select * from products;

-- Exercise 6
-- YOu would get an error, for instance, CHECK constraint failed: