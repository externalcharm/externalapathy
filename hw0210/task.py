# 1. Дано число.
# Если оно меньше 7, то вывести Yes, если больше 10, то вывести No, если равно 9, то вывести Error.
num = int(input("Введите число:"))
if num < 7:
    print("Yes")
elif num > 10:
    print("No")
else:
    num = 9
    print("Error")
