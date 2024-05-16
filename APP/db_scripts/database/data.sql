CREATE TABLE sizes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255)
);

CREATE TABLE statuses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50)
);

CREATE TABLE categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255)
);

CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255),
    size_id INT,
    price INT,
    quantity_in_stock INT,
    category_id INT,
    FOREIGN KEY (category_id) REFERENCES categories(id)
    FOREIGN KEY (size_id) REFERENCES sizes(id)
);

CREATE TABLE supplies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data DATE,
    quantity INT,
    product_id INT,
    FOREIGN KEY (product_id) REFERENCES products(id)
);

CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255)
);

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255),
    addres VARCHAR(255),
    login VARCHAR(50),
    password VARCHAR(50),
    post_id INT,
    FOREIGN KEY (post_id) REFERENCES posts(id),
    UNIQUE (password) ON CONFLICT IGNORE
);

CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    comment TEXT,
    data DATE,
    price INT,
    quantity INT,
    product_id INT,
    seller_id INT,
    bayer_id INT,
    status_id INT,
    FOREIGN KEY (product_id) REFERENCES products(id),
    FOREIGN KEY (seller_id) REFERENCES users(id),
    FOREIGN KEY (bayer_id) REFERENCES users(id),
    FOREIGN KEY (status_id) REFERENCES statuses(id)
);


INSERT INTO statuses (id, name) VALUES
(1, 'В обработке'),
(2, 'Выдан');

INSERT INTO sizes (id, name) VALUES
(1, 'XXS'),
(2, 'XS'),
(3, 'S'),
(4, 'M'),
(5, 'L'),
(6, 'XL'),
(7, 'XXL');

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

INSERT INTO products (id, name, size_id, price, quantity_in_stock, category_id) VALUES
(1, 'Футболка с принтом', 4, 2000, 24, 1),
(2, 'Футболка с принтом', 3, 2000, 30, 1),
(3, 'Белая футболка', 4, 1500, 14, 1),
(4, 'Белая футболка', 5, 1500, 10, 1),
(5, 'Брюки', 6, 4000, 22, 2),
(6, 'Брюки', 1, 4000, 18, 2),
(7, 'Платье', 2, 6000, 11, 3),
(8, 'Платье', 3, 6000, 9, 3),
(9, 'Рубашка', 4, 3009, 16, 4),
(10, 'Рубашка', 7, 3000, 15, 4),
(11, 'Юбка', 3, 5000, 8, 5),
(12, 'Юбка', 2, 5000, 7, 5),
(13, 'Куртка', 3, 8000, 5, 6),
(14, 'Куртка', 4, 8000, 3, 6),
(15, 'Джинсы', 4, 3400, 13, 7),
(16, 'Джинсы', 3, 3400, 15, 7),
(17, 'Пиджак', 6, 5000, 4, 8),
(18, 'Пиджак', 3, 5000, 6, 8),
(19, 'Шорты', 4, 1500, 29, 9),
(20, 'Шорты', 3, 1500, 27, 9),
(21, 'Пальто', 2, 12000, 8, 10),
(22, 'Пальто', 3, 12000, 6, 10);

INSERT INTO posts (id, name) VALUES
(1, 'Директор'),
(2, 'Кассир'),
(3, 'Покупатель');

INSERT INTO users (id, name, addres, login, password, post_id) VALUES
(1, 'Александр', 'шоссе Будапештсткая, 73', 'admin', 'admin', 1),
(2, 'Сергей', 'пр. Чехова, 20', 'kassir1', 'kassir1', 2),
(3, 'Марина', 'ул. Гоголя, 26', 'kassir2', 'kassir2', 2),
(4, 'Евгений', 'пер. Ленина, 30', 'kassir3', 'kassir3', 2),
(5, 'Дмитрий', 'проезд Балканская, 53', 'kassir4', 'kassir4', 2),
(6, 'Даниил', 'пр. Балканская, 08', 'user1', 'user1', 3),
(7, 'Василий', 'проезд Ленина, 95', 'user2', 'user2', 3),
(8, 'Кирилл', 'ул. Ладыгина, 25', 'user3', 'user3', 3),
(9, 'Кристина', 'пер. Гоголя, 78', 'user4', 'user4', 3);