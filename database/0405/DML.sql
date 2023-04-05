-- DML.sql

-- CREATE TABLE users (
--   first_name TEXT NOT NULL,
--   last_name TEXT NOT NULL,
--   age INTEGER NOT NULL,
--   country TEXT NOT NULL,
--   phone TEXT NOT NULL,
--   balance INTEGER NOT NULL,
-- );

CREATE TABLE users(
    name TEXT NOT NULL,
    phoneNumber TEXT NOT NULL,
    balance TEXT NOT NULL,
    age INTEGER,
    gender TEXT
);

SELECT name, age, balance FROM users
ORDER BY age, balance DESC;