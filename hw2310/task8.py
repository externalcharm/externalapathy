vibor = ("yes", "no")
name = input("Введите имя того кого хотите пригласить: ")
name1 = input("Введите имя того кого хотите пригласить: ")
name2 = input("Введите имя того кого хотите пригласить: ")
invList = [name, name1, name2]
while True:
    tname = input("Хотите ли вы добавить еще одно имя?: yes/no  ")

    if tname == 'yes':
        tname1 = input("Введите имя того кого хотите пригласить: ")
        invList.append(tname1)

    elif tname == 'no':
        print("Кол-во приглашенных людей, ", len(invList))
        break
