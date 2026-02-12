CREATE DATABASE IF NOT EXISTS customers_orders_db;

USE customers_orders_db;

CREATE TABLE IF NOT EXISTS customers(
    customerNumber INT PRIMARY KEY,
    customerName VARCHAR(250),
    contactLastName VARCHAR(250),
    contactFirstName VARCHAR(250),
    phone VARCHAR(250),
    addressLine1 VARCHAR(250),
    addressLine2 VARCHAR(250),
    city VARCHAR(250),
    state VARCHAR(250),
    postalCode VARCHAR(250),
    country VARCHAR(250),
    salesRepEmployeeNumber INT,
    creditLimit FLOAT
);

CREATE TABLE IF NOT EXISTS orders(
    orderNumber INT PRIMARY KEY,
    orderDate VARCHAR(250),
    requiredDate VARCHAR(250),
    shippedDate VARCHAR(250),
    status VARCHAR(250),
    comments VARCHAR(250),
    customerNumber INT
    FOREIGN KEY (customerNumber) REFERENCES customers(customerNumber)
);
