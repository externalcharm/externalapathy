name = input("Введите имя того кого хотите пригласить: ").capitalize()
name1 = input("Введите имя того кого хотите пригласить: ").capitalize()
name2 = input("Введите имя того кого хотите пригласить: ").capitalize()
invList = [name, name1, name2]
for names in invList:
    print(name)
listname = input("Введите имя из списка: ").capitalize()
if listname in invList:
    print(invList.index(listname))
userChoice = input("Хотите ли вы чтобы этот чел. присутствовал на вечеринке?: yes/no ")
if userChoice == 'yes':
    print(invList)
elif userChoice == 'no':
    invList.remove(listname)
    print(invList)
