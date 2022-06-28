#Завдання 1
x = int(input())
y = int(input())

def sportecus(x, y):
    day = 0

    while x < y:
        x += 0.1*x
        day += 1
        print(x)

    return day


print(sportecus(x, y))


#Завдання 2
our_number = int(input('Введите целое неотрицательное число с нулём в конце: '))


def list_maker(x):
    y = list()
    b = 0
    while x > 0:
        y.append(x % 10)
        x = (x - (x % 10)) // 10

    map(int, y)
    y.reverse()

    return y


def get_numbers_amount(x):
    y = 0
    for index, values in enumerate(list_maker(x)):
        y += 1

    return y - 1

def get_all_sum(x):
    y = 0
    for index, values in enumerate(list_maker(x)):
        y += values

    return y


def get_multiply(x):
    y = 1

    b = list(enumerate(list_maker(x)))
    del b[len(str(x))-1]

    for index, values in b:
        y *= values

    return y


def get_average(x):
    return get_all_sum(x) / get_numbers_amount(x)


def get_highest(x):
    b = list_maker(x)
    b.sort()
    max_int = b[len(b)-1]

    return max_int, list_maker(x//10).index(max_int)+1


def get_even_and_odd_amount(x):
    even = 0
    odd = 0

    for i in list_maker(x//10):
        if i % 2 == 0:
            even += 1
        else:
            odd += 1

    return even, odd


def get_second_max_int(x):
    y = list_maker(x//10)
    y.sort()
    max_int = get_highest(our_number)[0]

    while max_int in y:
        y.remove(max_int)

    y.reverse()

    return y[0]


def get_number_of_highest(x):
    max_int = get_highest(our_number)[0]
    b = 0

    for i in list_maker(x//10):
        if i == max_int:
            b += 1

    return b


print('Количество цифр: ' + str(get_numbers_amount(our_number)))
print('Сумма всех цифр: ' + str(get_all_sum(our_number)))
print('Умножение всех цифр: ' + str(get_multiply(our_number)))
print('Среднее арифметическое: ' + str(get_average(our_number)))
print('Самое большое и его положение: ' + str(get_highest(our_number)))
print('Количество чётных и не чётных: ' + str(get_even_and_odd_amount(our_number)))
print('Второе самое больше число: ' + str(get_second_max_int(our_number)))
print('Количество самых больших чисел: ' + str(get_number_of_highest(our_number)))


#Завдання 3
a = int(input())
b = int(input())


def a_to_b(our_number, y):
    s = str()
    if our_number < y:
        for i in range(our_number, y+1):
            s += str(i)
    else:
        for i in range(y, our_number+1)[::-1]:
            s += str(i)

    print(s)


a_to_b(a, b)


#Завдання 4
our_number = int(input('Input n<=9: '))


def stairs(our_number):
    b = str()
    for i in range(1, our_number+1):
        b += str(i)
        print(b)

    return b


stairs(our_number)

#Завдання 5
ryadok = list(input())


def get_third_symbol(our_number): #a
    return our_number[2]


def get_second_to_last_symbol(our_number): #b
    return our_number[len(our_number)-2]


def get_first_five_symbols(our_number): #c
    return our_number[0], our_number[1], our_number[2], our_number[3], our_number[4]


def get_except_two_last_symbols(our_number): #d
    b = list()

    for i in range(len(our_number)-2):
        b.append(our_number[i])
    return b


def get_even_index_symbols(our_number): #e
    b = list(our_number[::2])
    return b


def get_odd_index_symbols(our_number): #f
    b = list()
    for index, values in enumerate(our_number):
        if index % 2 != 0:
            b.append(our_number[index])
    return b


def get_reverced_symbols(our_number): #g
    b = list(our_number[::-1])
    return b


def get_all_symbols_reverced_step_1(our_number): #h
    return list(reversed(get_even_index_symbols(our_number)))


print('Третий символ: ' + str(get_third_symbol(ryadok)))
print('Предпоследний символ:' + str(get_second_to_last_symbol(ryadok)))
print('Первые пять символов: ' + str(get_first_five_symbols(ryadok)))
print('Вся строка, кроме последних двух:' + str(get_except_two_last_symbols(ryadok)))
print('Символы с парными  индексами: ' + str(get_even_index_symbols(ryadok)))
print('Символы с непарными индексами: ' + str(get_odd_index_symbols(ryadok)))
print('Символы в обратном порядке: ' + str(get_reverced_symbols(ryadok)))
print('Символы в обратном порядке через один: ' + str(get_all_symbols_reverced_step_1(ryadok)))
print('Длинна строки: ' + str(len(ryadok)))


# Завдання 6
our_number = int(input())


def highest_neighbor_number(our_number):
    y = list()
    b = 0
    while our_number > 0:
        y.append(our_number % 10)
        our_number = (our_number - (our_number % 10)) // 10

    for i in range(len(y)-1):
        if y[i-1] < y[i] > y[i+1]:
            b += 1
    return b


print(highest_neighbor_number(our_number))


# Завдання 7
list_1 = int(input('Input one list of integers: '))
list_2 = int(input('Input second list of integers: '))


def list_maker(our_number):
    y = list()
    while our_number > 0:
        y.append(our_number % 10)
        our_number = (our_number - (our_number % 10)) // 10
    reversed(y)
    return y


def get_list_of_commons(our_number, y):  # общие для двух
    list_of_commons = []
    for our_number in our_number:
        if our_number in y:
            list_of_commons.append(our_number)

    return set(list_of_commons)


def get_list_of_uniques_in_list_1(our_number, y):  # есть в первом, но нет во втором
    list_of_uniques_in_list_1 = []
    for our_number in our_number:
        if our_number not in y:
            list_of_uniques_in_list_1.append(our_number)

    return set(list_of_uniques_in_list_1)


def get_list_of_uniques_for_both(our_number, y):  # уникальные для обоих
    list_of_uniques_for_both = list()
    a = list(our_number + y)

    for i in a:
        if a.count(i) == 1:
            list_of_uniques_for_both.append(i)

    return list_of_uniques_for_both


print(get_list_of_commons(list_maker(list_1), list_maker(list_2)))
print(get_list_of_uniques_in_list_1(list_maker(list_1), list_maker(list_2)))
print(get_list_of_uniques_for_both(list_maker(list_1), list_maker(list_2)))
