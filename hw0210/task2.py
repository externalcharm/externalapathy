# 4. Робот может перемещаться в четырех направлениях («11» — север, «12» — запад,
# «13» — юг, «14» — восток) и принимать три цифровые команды:
# 0 — продолжать движение, 1 — поворот налево, –1 — поворот направо.
# Дан число (11, 12, 13 или 14) — исходное направление робота и целое число N (0, 1 или -1) — посланная ему команда.
# Вывести направление робота после выполнения полученной команды (то есть север, запад, юг или восток).
print("Направления: Север - 11, Запад - 12, Юг - 13, Восток - 14")
direct = int(input("Введите направление робота: "))
print("Команды: 0 — продолжать движение, 1 — поворот налево, –1 — поворот направо")
command = int(input("Введите команду: "))

if direct == 11:
    if command == 0:
        print("Север")
    elif command == 1:
        print("Запад")
    elif command == -1:
        print("Восток")

elif direct == 12:
    if command == 0:
        print("Запад")
    elif command == 1:
        print("Юг")
    elif command == -1:
        print("Север")

elif direct == 13:
    if command == 0:
        print("Юг")
    elif command == 1:
        print("Восток")
    elif command == -1:
        print("Запад")

elif direct == 14:
    if command == 0:
        print("Восток")
    elif command == 1:
        print("Север")
    elif command == -1:
        print("Юг")
