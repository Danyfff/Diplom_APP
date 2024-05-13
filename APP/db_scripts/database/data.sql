CREATE TABLE categories (
    id INT PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE products (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    size VARCHAR(255),
    price INT,
    quantity_in_stock INT,
    category_id INT,
    FOREIGN KEY (category_id) REFERENCES categories(id)
);

CREATE TABLE supplies (
    id INT PRIMARY KEY,
    data DATE,
    quantity INT,
    products_id INT,
    FOREIGN KEY (products_id) REFERENCES products(id)
);

CREATE TABLE posts (
    id INT PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE users (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    addres VARCHAR(255),
    login VARCHAR(50),
    password VARCHAR(50),
    post_id INT,
    FOREIGN KEY (post_id) REFERENCES posts(id)
);

CREATE TABLE orders (
    id INT PRIMARY KEY,
    comment TEXT,
    data DATE,
    price INT,
    quantity INT,
    products_id INT,
    seller_id INT,
    bayer_id INT,
    FOREIGN KEY (products_id) REFERENCES products(id),
    FOREIGN KEY (seller_id) REFERENCES users(id),
    FOREIGN KEY (bayer_id) REFERENCES users(id)
);

INSERT INTO categories (id, name) VALUES
(1, 'Футболки'),
(2, 'Брюки'),
(3, 'Платья'),
(4, 'Рубашки'),
(5, 'Юбки'),
(6, 'Куртки'),
(7, 'Джинсы'),
(8, 'Пиджаки'),
(9, 'Шорты'),
(10, 'Пальто');

INSERT INTO products (id, name, size, price, quantity_in_stock, category_id) VALUES
(1, 'Футболка с принтом', 'S', 2000, 24, 1),
(2, 'Футболка с принтом', 'M', 2000, 30, 1),
(3, 'Белая футболка', 'M', 1500, 14, 1),
(4, 'Белая футболка', 'S', 1500, 10, 1),
(5, 'Брюки', 'S', 4000, 22, 2),
(6, 'Брюки', 'M', 4000, 18, 2),
(7, 'Платье', 'S', 6000, 11, 3),
(8, 'Платье', 'M', 6000, 9, 3),
(9, 'Рубашка', 'S', 3009, 16, 4),
(10, 'Рубашка', 'M', 3000, 15, 4),
(11, 'Юбка', 'S', 5000, 8, 5),
(12, 'Юбка', 'M', 5000, 7, 5),
(13, 'Куртка', 'S', 8000, 5, 6),
(14, 'Куртка', 'M', 8000, 3, 6),
(15, 'Джинсы', 'S', 3400, 13, 7),
(16, 'Джинсы', 'M', 3400, 15, 7),
(17, 'Пиджак 1', 'S', 5000, 4, 8),
(18, 'Пиджак 2', 'M', 5000, 6, 8),
(19, 'Шорты 1', 'S', 1500, 29, 9),
(20, 'Шорты 2', 'M', 1500, 27, 9),
(21, 'Пальто 1', 'S', 12000, 8, 10),
(22, 'Пальто 1', 'M', 12000, 6, 10);

INSERT INTO posts (id, name) VALUES
(1, 'Директор'),
(2, 'Кассир'),
(3, 'Покупатель');

INSERT INTO users (id, name, addres, login, password, post_id) VALUES
(1, 'Директор', 'Инкогнито', 'admin', 'admin', 1),
(2, 'Кассир 1', 'Address 2', 'kassir1', 'kassir1', 2),
(3, 'Кассир 2', 'Address 3', 'kassir2', 'kassir2', 2),
(4, 'Кассир 3', 'Address 4', 'kassir3', 'kassir3', 2),
(5, 'Кассир 4', 'Address 5', 'kassir4', 'kassir4', 2),
(6, 'User 1', 'Address 6', 'user1', 'user1', 3),
(7, 'User 2', 'Address 7', 'user2', 'user2', 3),
(8, 'User 3', 'Address 8', 'user3', 'user3', 3),
(9, 'User 4', 'Address 9', 'user4', 'user4', 3);