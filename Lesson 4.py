#Завдання 1
x = int(input())
y = int(input())

def sportecus(x, y):
    day = 0

    while x < y:
        x *= 1.1
        day += 1
        print(x)

    return day


print(sportecus(x, y))


# Завдання 2
def get_our_number():
    number = []
    while True:
        number_to_input = input()
        if int(number_to_input) != 0:
            number.append(int(number_to_input))
        else:
            break

    return number  # выходит список


our_number = get_our_number()


def get_numbers_amount(x):
    y = 0
    for i in x:
        y += 1
    return y


def get_all_sum(x):
    return sum(x)


def get_multiply(x):
    y = 1
    for i in x:
        y *= i
    return y


def get_average(x):
    return get_all_sum(x)/get_numbers_amount(x)


def get_highest(x):
    max_int = max(x)
    max_index = x.index(max_int)
    return max_int, max_index+1


def get_even_and_odd_amount(x):
    even = 0
    odd = 0

    for i in x:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd


def get_second_max_int(x):
    y = x
    y.remove(max(x))
    return max(y)


def get_amount_of_highest(x):
    y = 0
    for i in x:
        if i == max(x):
            y += 1
    return y


print('Количество цифр: ' + str(get_numbers_amount(our_number)))
print('Сумма всех цифр: ' + str(get_all_sum(our_number)))
print('Умножение всех цифр: ' + str(get_multiply(our_number)))
print('Среднее арифметическое: ' + str(get_average(our_number)))
print('Самое большое и его положение: ' + str(get_highest(our_number)))
print('Количество чётных и не чётных: ' + str(get_even_and_odd_amount(our_number)))
print('Второе самое больше число: ' + str(get_second_max_int(our_number)))
print('Количество самых больших чисел: ' + str(get_amount_of_highest(our_number)))

#Завдання 3
a = int(input())
b = int(input())


def a_to_b(x, y):
    s = str()
    if x < y:
        for i in range(x, y + 1):
            s += str(i)
    else:
        for i in range(y, x + 1)[::-1]:
            s += str(i)

    print(s)


a_to_b(a, b)

#Завдання 4
x = int(input('Input n<=9: '))


def stairs(x):
    b = str()
    for i in range(1, x+1):
        b += str(i)
        print(b)

    return b


stairs(x)


#Завдання 5
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
    for index, values in enumerate(x):
        if index % 2 != 0:
            b.append(x[index])
    return b


def get_reverced_symbols(x): #g
    b = list(x[::-1])
    return b


def get_all_symbols_reverced_step_1(x): #h
    return list(reversed(get_even_index_symbols(x)))


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


highest_neighbor_number(int(input()))
"""

"""# Завдання 7
set_1 = set(input('Input one list of integers: '))
set_2 = set(input('Input second list of integers: '))


def get_list_of_commons(x, y):  # общие для двух
    z = x.intersection(y)
    return print(z)


def get_list_of_uniques_set_1(x, y):  # есть в первом, но нет во втором
    z = x.difference(y)
    return print(z)


def get_list_of_uniques_for_both(x, y):  # уникальные для обоих
    z = x.difference(y)
    z.update(y.difference(x))
    return print(z)


get_list_of_commons(set_1, set_2)
get_list_of_uniques_set_1(set_1, set_2)
get_list_of_uniques_for_both(set_1, set_2)
