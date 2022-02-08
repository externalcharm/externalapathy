TVshows = ["Discovery", "TNT", "Cartoon Network", "Karusel"]
for shows in TVshows:
    print(shows)
userShow = input("Введите своё TV шоу: ")
userListPos = int(input("Введите желаемую  позицию в списке:"))
TVshows.insert(userListPos, userShow)
print(TVshows)
