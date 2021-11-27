class Buyer:
    def __init__(self):
        self.surname = None
        self.name = None
        self.pathron = None
        self.card = None
        self.bank = None

    def getdata(self):
        surname = input("Введите фамилию: ")
        name = input("Введите имя: ")
        pathron = input("Введите отчество :")
        card = int(input("Введите номер карты: "))
        bank = int(input("Введите номер банк. счета: "))
        buyers = [surname, name, pathron, card, bank]
        return str(buyers)


buyer1 = Buyer()
print(buyer1.getdata())
