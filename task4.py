'''
Создать информационную систему позволяющую работать с сотрудниками
некой компании \ студентами вуза \ учениками школы
'''

database = {}
db = {'parents': 1, 'children': 2, 'city': 3}


def reading_file_to_dict(number_file):
    with open(f'{number_file}.txt', 'r', encoding='utf-8') as file_1:
        data = [i.split('\n')[0] for i in file_1.readlines()]
        # print(data)
        database[number_file] = []
        for i in data:
            database[number_file].append(tuple(i.split(';')))


def print_children(second_name):
    id = [i[0] for i in database[db['parents']] if second_name in i][0]
    deti = [i for i in database[db['children']] if id == i[1]]
    print(*[' '.join(i[2:4]) + '\n' for i in deti])

    #  n='Ivanov'
       #for i in database[1]:
        #    if i[2]==n:
         #     for j in database[2]:
          #      if j[1]==i[0]:
          #          print(f'{j[2]} {j[3]}')

def print_city(cit):
    id = [i[0] for i in database[db['parents']] if cit in i][0]
    city = [i for i in database[db['city']] if id == i[0]]
    print(f'{cit} city:',*[' '.join(i[1:]) + '\n' for i in city])

reading_file_to_dict(1)
reading_file_to_dict(2)
reading_file_to_dict(3)
print(database)
print_children('Ivanov')
print_children('Efremov')
print_city('Efremov')
print_city('Ivanov')
# Создать решение для вывода детей по фамилии