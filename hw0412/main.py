from collections import Counter

file = open('pwd.txt', 'r')

passwords = Counter()
for line in file:
    password = line.split(';')
    password.reverse()
    passwords[password[0]] += 1

for password in passwords.most_common(10):
    print(password[1], password[0], sep=': ', end="")

file.close()
