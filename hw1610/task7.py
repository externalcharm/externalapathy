word = input("Введите слово для перевода: ")
vowles = ['a', 'e', 'u', 'y', 'i', 'o']


def translate(word):
    first = word[0]
    if first in vowles:
        word = word.lower()
        word += "way"
        return word
    else:
        word = word.lower()

        for letter in word:
            if letter in vowles:
                lindex = word.index(letter)
                break

        word = word[lindex:] + word[:lindex] + "ay"
        return word


print(translate(word))
