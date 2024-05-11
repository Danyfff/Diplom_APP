CREATE TABLE variety_thing (
    id INT PRIMARY KEY,
    name_variety VARCHAR(255)
);

CREATE TABLE things (
    id INT PRIMARY KEY,
    name_clothe VARCHAR(255),
    price INT,
    FOREIGN KEY (variety_thing) REFERENCES variety_thing(id)
);

CREATE TABLE statuses (
    id INT PRIMARY KEY,
    name_status VARCHAR(255)
);

CREATE TABLE users (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    addres VARCHAR(255),
    login VARCHAR(50),
    password VARCHAR(50),
    FOREIGN KEY (id_status) REFERENCES statuses(id)
);

CREATE TABLE orders (
    id INT PRIMARY KEY,
    comment TEXT,
    data_create DATE,
    FOREIGN KEY (id_seller) REFERENCES users(id),
    FOREIGN KEY (id_buyer) REFERENCES users(id),
    FOREIGN KEY (items) REFERENCES types_faults(tip_faults_id)
    FOREIGN KEY (id_user) REFERENCES users(id),
    FOREIGN KEY (id_client) REFERENCES clients(client_id)
);


INSERT INTO variety_thing (id, name_variety) VALUES 
(1, 'платье'),
(2, 'брюки'),
(3, 'рубашка');

INSERT INTO things (id, name_clothe, price, variety_thing) VALUES 
(1, 'платье1', 1000, 1),
(2, 'брюки1', 800, 2),
(3, 'рубашка1', 600, 3);

INSERT INTO statuses (id, name_status) VALUES 
(1, 'Директор'),
(2, 'Продавец'),
(3, 'Покупатель');

INSERT INTO users (id, name, addres, login, password, id_status) VALUES 
(1, 'Иванова Мария', 'ул. Ленина, д.1, кв. 5', 'maria', 'pass123', 1),
(2, 'Петров Иван', 'ул. Пушкина, д.2, кв. 10', 'ivan', 'pass456', 2),
(3, 'Сидорова Ольга', 'ул. Маяковского, д.3, кв. 15', 'olya', 'pass789', 3);

INSERT INTO orders (id, comment, data_create, id_seller, id_buyer, items, id_user, id_client) VALUES 
(1, 'Быстро нужно', '2024-05-11', 1, 2, 1, 3, 4),
(2, 'Пожалуйста подождите', '2024-05-12', 2, 1, 3, 2, 1);