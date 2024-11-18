-- This is how you comment in SQL
-- An SQL Script
/* This is
a multiline comment
in sql*/

-- Creatig a Database
CREATE DATABASE IF NOT EXISTS `tech4girls`;

-- Showing a Database
SHOW DATABASES;

-- Using a Database
USE tech4girls;

-- CREATING A TABLE
CREATE TABLE IF NOT EXISTS backend_class (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(256) NOT NULL,
    age INT NOT NULL,
    email VARCHAR(256) UNIQUE NOT NULL
);

SHOW TABLES;

INSERT INTO backend_class (first_name, last_name, age, email)
VALUES ('Rhoda', 'Oduro-Nyarko', 22, 'rhodalee.dev@gmail.com');

SELECT * FROM backend_class;