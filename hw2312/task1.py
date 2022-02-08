def printnum(a, b):
    if a and b == 1:
        print(1, end=' ')
    elif a < b:
        printnum(a, b - 1)
        print(b, end=' ')
    else:
        print(a, end=' ')
        printnum(a - 1, b)


printnum(6, 5)
