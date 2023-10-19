-- a script that creates the table unique_id on your MySQL server
CREATE TABLE IF NOT EXISTS id_not_null(
    id INT NOT NULl DEFAULT 1 UNIQUE,
    name VARCHAR(256),
);
