CREATE DATABASE todo_db;

USE todo_db;

CREATE TABLE task (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    status VARCHAR(10) DEFAULT 'Pending'
);
