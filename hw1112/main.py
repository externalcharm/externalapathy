menu = []
with open('cats.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if line[:line.index(' ')].isdigit() and \
                line[line.rindex(' ') + 1:].isdigit():
            menu.append({
                'id': int(line[:line.index(' ')]),
                'title': line[line.index(' '):line.rindex(' ') + 1].strip(),
                'id_parent': int(line[line.rindex(' ') + 1:])
            })
print(menu)


def print_menu(list, item, deep, id_parent):
    print('\t' * deep, item['title'])
    if not item['id'] == id_parent:
        for num in range(len(list)):
            if list[num]['id_parent'] == item['id']:
                print_menu(list, list[num], deep + 1, id_parent)
    else:
        exit()


for num in range(len(menu)):
    if menu[num]['id_parent'] == 0:
        print_menu(menu, menu[num], 0, 0)
