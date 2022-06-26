#Завдання 5
#Попробовать написать всё через лямбда функции
ryadok = list(input())


def get_third_symbol(x): #a
    return x[2]


def get_second_to_last_symbol(x): #b
    return x[len(x)-2]


def get_first_five_symbols(x): #c
    return x[0], x[1], x[2], x[3], x[4]


def get_except_two_last_symbols(x): #d
    b = list()

    for i in range(len(x)-2):
        b.append(x[i])
    return b


def get_even_index_symbols(x): #e
    b = list(x[::2])
    return b


def get_odd_index_symbols(x): #f
    b = list()

    return b


def get_reverced_symbols(x): #g
    b = list(x[::-1])
    return b


def get_all_symbols_reverced_step_1(x): #h
    b = list(x.reverse())

    return b


print('Третий символ: ' + str(get_third_symbol(ryadok)))
print('Предпоследний символ:' + str(get_second_to_last_symbol(ryadok)))
print('Первые пять символов: ' + str(get_first_five_symbols(ryadok)))
print('Вся строка, кроме последних двух:' + str(get_except_two_last_symbols(ryadok)))
print('Символы с парными  индексами: ' + str(get_even_index_symbols(ryadok)))
print('Символы с непарными индексами: ' + str(get_odd_index_symbols(ryadok)))
print('Символы в обратном порядке: ' + str(get_reverced_symbols(ryadok)))
print('Символы в обратном порядке через один: ' + str(get_all_symbols_reverced_step_1(ryadok)))
print('Длинна строки: ' + str(len(ryadok)))


"""# Завдання 6
x = int(input())


def highest_neighbor_number(x):
    y = list()
    b = 0
    while x > 0:
        y.append(x % 10)
        x = (x - (x % 10)) // 10

    for i in range(len(y)-1):
        if y[i-1] < y[i] > y[i+1]:
            b += 1
    return b


print(highest_neighbor_number(x))


# Завдання 7
list_1 = int(input('Input one list of integers: '))
list_2 = int(input('Input second list of integers: '))


def list_maker(x):
    y = list()
    while x > 0:
        y.append(x % 10)
        x = (x - (x % 10)) // 10
    reversed(y)
    return y


def get_list_of_commons(x, y):  # общие для двух
    list_of_commons = []
    for x in x:
        if x in y:
            list_of_commons.append(x)

    return set(list_of_commons)


def get_list_of_uniques_in_list_1(x, y):  # есть в первом, но нет во втором
    list_of_uniques_in_list_1 = []
    for x in x:
        if x not in y:
            list_of_uniques_in_list_1.append(x)

    return set(list_of_uniques_in_list_1)


def get_list_of_uniques_for_both(x, y):  # уникальные для обоих
    list_of_uniques_for_both = list()
    a = list(x + y)

    for i in a:
        if a.count(i) == 1:
            list_of_uniques_for_both.append(i)

    return list_of_uniques_for_both


print(get_list_of_commons(list_maker(list_1), list_maker(list_2)))
print(get_list_of_uniques_in_list_1(list_maker(list_1), list_maker(list_2)))
print(get_list_of_uniques_for_both(list_maker(list_1), list_maker(list_2)))
"""