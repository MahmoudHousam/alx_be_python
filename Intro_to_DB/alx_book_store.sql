-- create the database
CREATE DATABASE IF NOT EXISTS alx_book_store;

-- use database
USE alx_book_store;

-- create Books table
CREATE TABLE IF NOT EXISTS Books (
    book_id INT PRIMARY KEY,
    title NOT NULL VARCHAR(130),
    author_id INT NOT NULL,
    price,
    publication_date DATE,
    FOREIGN KEY (author_id) REFERENCES Authors(author_id)
);

-- create Authors table
CREATE TABLE IF NOT EXISTS Authors (
    author_id INT PRIMARY KEY,
    author_name VARCHAR(215),
);

-- create Customers table
CREATE TABLE IF NOT EXISTS Customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(215),
    email VARCHAR(215),
    address TEXT
);

-- create Orders table
CREATE TABLE IF NOT EXISTS Orders (
    order_id INT PRIMARY KEY,
    customer_id INT NOT NULL VARCHAR(215),
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

-- create Orders_Dtails table
CREATE TABLE IF NOT EXISTS Orders_Dtails (
    order_id INT PRIMARY KEY,
    book_id INT NOT NULL VARCHAR(215),
    quantity,
    FOREIGN KEY (order_id) REFERENCES Orders(customer_id),
    FOREIGN KEY (book_id) REFERENCES Books(book_id),
);
