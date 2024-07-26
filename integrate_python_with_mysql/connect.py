import mysql.connector
from mysql.connector import Error


# Function to create a database connection
def create_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name, user=user_name, passwd=user_password
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection


# Function to create a database
def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


# Function to execute a query
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


# Function to fetch the result of a query
def fetch_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


# Connection details
host = "localhost"
user = "root"
password = "my_password"

# Connect to MySQL server
connection = create_connection(host, user, password)

# Create a new database
create_database_query = "CREATE DATABASE test_db"
create_database(connection, create_database_query)

# Connect to the newly created database
connection.database = "test_db"

# Create a new table
create_table_query = """
CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    hire_date DATE NOT NULL
)
"""
execute_query(connection, create_table_query)

# Insert data into the table
insert_data_query = """
INSERT INTO employees (first_name, last_name, email, hire_date) VALUES
('John', 'Doe', 'john.doe@example.com', '2020-01-15'),
('Jane', 'Smith', 'jane.smith@example.com', '2019-03-22'),
('Mike', 'Johnson', 'mike.johnson@example.com', '2021-06-01')
"""
execute_query(connection, insert_data_query)

# Query the data
select_data_query = "SELECT * FROM employees"
employees = fetch_query(connection, select_data_query)

# Print the results
for employee in employees:
    print(employee)

# Close the connection
connection.close()
