ThreeDigNumbers = [111, 222, 333, 444]

for num in ThreeDigNumbers:
    print(num)

usernum = int(input("Введите число из трех цифр из списка: "))
if usernum in ThreeDigNumbers:
    print(ThreeDigNumbers.index(usernum))
else:
    print("That is not in the list")
