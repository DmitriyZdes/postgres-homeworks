-- SQL-команды для создания табли

CREATE TABLE employees

( 		employee_id int PRIMARY KEY,
  		first_name varchar(20) not null,
  		last_name varchar(20) not null,
  		operation_id int UNIQUE

);

CREATE TABLE customers

( 		customer_id varchar(20) PRIMARY KEY,
  		nickname varchar(20),
  		operation_id int UNIQUE

);

CREATE TABLE orders

( 		order_id int UNIQUE,
  		operation_date date not null
        employee_id int PRIMARY KEY REFERENCES employees(employee_id)
        customer_id varchar(20) REFERENCES customers(customer_id)

)
