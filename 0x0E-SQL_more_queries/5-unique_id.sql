--A script that creates the table unique_id on your MySQL server.
-- creates a table unique_id with default 1
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
