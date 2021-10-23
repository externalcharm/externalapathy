ThreeDigNumbers = ["000", "111", "222", "333"]
while True:

    for num in ThreeDigNumbers:
        print(num)

    usernum = int(input("Введите число из трех цифр из списка: "))
    if usernum == ThreeDigNumbers:
        print(ThreeDigNumbers[usernum])
# else:
#     print("That is not in the list")
