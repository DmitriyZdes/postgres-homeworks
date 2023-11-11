-- SQL-команды для создания табли

CREATE TABLE employees

( 		employer_id int PRIMARY KEY,
  		first_name varchar(20) not null,
  		last_name varchar(20) not null,
  		operation_id int UNIQUE

);

CREATE TABLE customers

( 		customer_id int PRIMARY KEY,
  		nickname varchar(20),
  		operation_id int UNIQUE

);

CREATE TABLE orders

( 		order_id int UNIQUE,
  		operation_date date not null

)
