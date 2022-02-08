usernum = int(input("Введите любое число: "))
usernum1 = int(input("Введите любое число: "))
usernum2 = int(input("Введите любое число: "))
nums = [usernum2, usernum1, usernum]
print(nums)
userTask = input("Хотите ли вы оставить последнее введенное число? yes/no")
if userTask == 'yes':
    print(nums)
elif userTask == 'no':
    nums.pop()
    print(nums)
