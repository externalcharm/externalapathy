name = input("Введите имя: ")

if len(name) < 5:
    surname = input("Введите фамилию: ")
    nameSurname = name + surname
    print(nameSurname.upper())
elif len(name) > 5:
    print (name.lower())

