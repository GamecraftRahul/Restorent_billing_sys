CREATE DATABASE IF NOT EXISTS restaurant_db;
USE restaurant_db;

CREATE TABLE IF NOT EXISTS items (
  item_id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  category VARCHAR(50),
  price DECIMAL(10,2)
);

INSERT INTO items (name, category, price) VALUES
('Margherita Pizza', 'Pizza', 249.00),
('Veg Burger', 'Burger', 129.00),
('Cold Coffee', 'Beverage', 79.00),
('Lemonade', 'Beverage', 59.00),
('Pasta Alfredo', 'Pasta', 199.00),
('Grilled Sandwich', 'Sandwich', 119.00),
('French Fries', 'Sides', 89.00),
('Caesar Salad', 'Salad', 159.00),
('Paneer Roll', 'Snacks', 99.00),
('Tandoori Pizza', 'Pizza', 299.00);

CREATE TABLE IF NOT EXISTS bills (
  bill_id INT AUTO_INCREMENT PRIMARY KEY,
  customer_name VARCHAR(100),
  total DECIMAL(10,2),
  date_time DATETIME DEFAULT CURRENT_TIMESTAMP
);
