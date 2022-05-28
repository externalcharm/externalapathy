CREATE TABLE IF NOT EXISTS menu(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name VARCHAR(255) NOT NULL,
    category VARCHAR(255) NOT NULL,
    image BLOB NOT NULL,
    price TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS reviews(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    author_review VARCHAR(255) NOT NULL,
    review VARCHAR(255) NOT NULL
);

INSERT INTO menu (product_name, category, price) VALUES
    ("Пицца маргарита", "pizza", "10$"),
    ("Пицца салями", "pizza", "8$"),
    ("Маки Роллы", "sushi", "5$"),
    ("Суши Калифорния", "sushi", "6$"),
    ("Картошка фри мал.", "snacks", "1$"),
    ("Картошка фри ср.", "snacks", "2$"),
    ("Картошка фри больш.", "snacks", "3$");

INSERT INTO reviews (author_review, review) VALUES
    ("Морж", "Отличная быстрая доставка 10\10"),
    ("Морской котик", "Отличное заведение, очень вкусно 10\10"),
    ("Кошак", "Вкусный кошачий корм 9\10");