CREATE TABLE IF NOT EXISTS calendar(
    abbreviated TEXT PRIMARY KEY,
    utter TEXT NOT NULL
);

INSERT INTO calendar (abbreviated, utter) VALUES
    ("Mon", "Понедельник"),
    ("Tue", "Вторник"),
    ("Wed", "Среда"),
    ("Thu", "Четверг"),
    ("Fri", "Пятница"),
    ("Sat", "Суббота"),
    ("Sun", "Воскресенье");
