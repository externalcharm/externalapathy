from random import randint
from random import choice


class Door:
    def __init__(self, instance):
        self.instance = instance

    def openDoor(self, hero):
        if isinstance(self.instance, Artefacts):
            hero.health += self.instance.force
        else:
            hero.health -= self.instance.damage


class Artefacts:
    def __init__(self):
        self.force = randint(10, 80)

    def __str__(self):
        return "Артефакт с " + str(self.force) + " хп"


class Monsters:
    def __init__(self):
        self.damage = randint(5, 100)

    def __str__(self):
        return "Монстр с " + str(self.damage) + " урона"


class Hero:
    def __init__(self, health):

        self.health = health

    def __str__(self):
        return "Здоровье героя:" + str(self.health)


# переменная с здоровьем героя
hero = Hero(25)
# двери
door = {}
for i in range(10):
    instances = [Artefacts(), Monsters()]  # переменная с артефактами и монстрами
    door[i] = Door(choice(instances))
# логика открывания дверей с выводом артефактов, монстров и здоровья героя
for i in range(10):
    door[i].openDoor(hero)
# проверка хп героя
    if hero.health > 1:
        print(hero)
        print(Artefacts(), Monsters())
        continue
    elif hero.health < 0:
        print(hero, '\n' "Ваш герой был убит, вы проиграли")
        print("За дверью был", Artefacts(), "и", Monsters())
        break
