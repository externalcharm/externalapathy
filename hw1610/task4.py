firstString = input("Введите первую строку стихотворения: ")
length = len(firstString)
print("Длина строки: ", length)
start = int(input("Введите начальную позицию: "))
end = int(input("Введите конечную позицию: "))
part = (firstString[start:end])
print(part)

