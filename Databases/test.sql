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

/* INSERT INTO backend_class (first_name, last_name, age, email)
VALUES ('Rhoda', 'Oduro-Nyarko', 22, 'rhodalee.dev@gmail.com'),
('Nana Afua Antwiwaa', 'Conduah', 19, 'anaconduah@st.ug.edu.gh'),
('Talatu', 'Nyande', 22, 'tnyande@gmail.com'); */


CREATE TABLE IF NOT EXISTS laptops (
    laptop_name VARCHAR(100) NOT NULL,
    laptop_number INT PRIMARY KEY,
    student_id INT NOT NULL,
    FOREIGN KEY (student_id) REFERENCES backend_class(student_id)
);

SHOW TABLES;

-- INSERT INTO laptops (laptop_name, laptop_number, student_id)
-- VALUES ('HP 14', 2020, 1);


UPDATE backend_class
SET age = 21, email = 'talatunyande@gmail.com'
WHERE first_name = 'Talatu';

DELETE FROM backend_class
WHERE first_name = 'Talatu';

SELECT * FROM backend_class;
SELECT * FROM laptops;
