"""#Завдання 1
import random


def is_prime(x):
    p = 0
    for i in range(1, 1000):
        if x % i == 0:
            p += 1

    if p == 2:
        return print(x, True)
    else:
        return print(x, False)


is_prime(random.randint(0, 1000))

#Завдання 2
def word_symbols_amount():
    s = input()
    words = 1
    symbols = 0

    for i in s:
        if i == ' ':
            words += 1

    for i in s:
        if i != ' ':
            symbols += 1

    return print(words, symbols)


word_symbols_amount()


#Завдання 3
import math

a = int(input('Перша сторона: '))
b = int(input('Друга сторона: '))
figure_type = int(input('Введіть 1, якщо трикутник і 2, якщо чотирикутник: '))


def triangle_area(x, y):
    z = round(math.hypot(x, y)) #находим сторону
    p = (x + y + z)/2
    s = math.sqrt(p * (p-x) * (p-y) * (p-z))
    return s


def quadrangle_area(x, y):
    return triangle_area(x, y) * 2


def area_printer(x):
    if x == 1:
        return print(triangle_area(a, b))
    elif x == 2:
        return print(quadrangle_area(a, b))


area_printer(figure_type)


#Завдання 4
a = input()


def odds_to_zero_count(x):
    y = []
    z = 0

    for index, values in enumerate(list(x)):
        if int(values) % 2 == 0:
            y.append(values)
        else:
            y.append(0)

    for i in y:
        if i == 0:
            z += 1

    return print(z)


odds_to_zero_count(a)


#Завдання 5
import math


def square(x):
    a = (x*4, x**2, x*math.sqrt(2))
    return a


print(square(int(input())))


#Завдання 6
a = {'first_color': 'Red', 'second_color': 'Green', 'third_color': None}


def dict_cleaner(x):
    y = {}

    for key, values in x.items():
        if values is not None:
            y.update({key: values})
    return print(y)


dict_cleaner(a)


#Завдання 7
def is_date(day, month, year):
    simple_year = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    leap_year = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    try:
        if year % 4 == 0 and year % 100 != 0 and year % 400 == 0:
            if day in range(leap_year[month]):
                return print(True)
            else:
                return print(False)
        elif day in range(simple_year[month]):
            return print(True)
        else:
            return print(False)
    except:
        print(False)


is_date(int(input('Введіть число: ')), int(input('Введіть місяць: ')), int(input('Введіть рік: ')))
"""
