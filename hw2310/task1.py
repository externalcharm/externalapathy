tuple1 = ("Belarus", "USA", "Africa", "Russia", "Nederlands")
for country in tuple1:
    print(country)
    userch = input("Введите название страны: ").capitalize()
    print(tuple1.index(userch))