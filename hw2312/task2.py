def yesorno(n):
    if n == 2:
        print("YES")
    elif n < 2:
        print("NO")
    else:
        yesorno(n/2)


yesorno(16)