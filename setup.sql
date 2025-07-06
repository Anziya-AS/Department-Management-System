-- Create the database
CREATE DATABASE IF NOT EXISTS department_db;
USE department_db;

-- Create the departments table
CREATE TABLE IF NOT EXISTS departments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

-- Create the employees table
CREATE TABLE IF NOT EXISTS employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    department_id INT,
    role VARCHAR(100),
    FOREIGN KEY (department_id) REFERENCES departments(id)
        ON DELETE CASCADE
);

-- Create the tasks table
CREATE TABLE IF NOT EXISTS tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id INT,
    task TEXT NOT NULL,
    status VARCHAR(50) DEFAULT 'Assigned',
    FOREIGN KEY (employee_id) REFERENCES employees(id)
        ON DELETE CASCADE
);
