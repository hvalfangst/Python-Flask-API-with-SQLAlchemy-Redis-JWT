-- Create table for users
CREATE TABLE IF NOT EXISTS users (
                                     user_id SERIAL PRIMARY KEY,
                                     first_name VARCHAR(50) NOT NULL,
                                     last_name VARCHAR(50) NOT NULL,
                                     phone_number VARCHAR(15),
                                     address VARCHAR(255),
                                     email VARCHAR(255) UNIQUE NOT NULL,
                                     password VARCHAR(200) UNIQUE NOT NULL,
                                     ssn VARCHAR(11) UNIQUE NOT NULL,
                                     access VARCHAR(6) NOT NULL
);


-- Create table for accounts
CREATE TABLE IF NOT EXISTS accounts (
                                        account_id SERIAL PRIMARY KEY,
                                        user_id INT REFERENCES users(user_id),
                                        account_number VARCHAR(12) UNIQUE NOT NULL,
                                        balance DECIMAL NOT NULL
);