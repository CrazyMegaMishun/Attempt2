#Завдання 1
import random


def is_prime(x):
    p = 0
    for i in range(1, 1000):
        if x % i == 0:
            p += 1

    if p == 2:
        return x, True
    else:
        return x, False


print(is_prime(random.randint(0, 1000)))

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

    return words, symbols


print(word_symbols_amount())


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
        return triangle_area(a, b)
    elif x == 2:
        return quadrangle_area(a, b)


print(area_printer(figure_type))


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

    return z


print(odds_to_zero_count(a))


#Завдання 5


def square(x):
    a = (x*4, x**2, x**0.5)
    return a


print(square(int(input())))


#Завдання 6
a = {'first_color': 'Red', 'second_color': 'Green', 'third_color': None}


def dict_cleaner(x):
    x.popitem()
    return x


print(dict_cleaner(a))


#Завдання 7
def is_date(day, month, year):
    calendar = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

    if year % 4 == 0 and year % 100 != 0:
        calendar[2] = 29

    try:
        if day in range(calendar[month] + 1):
            return print(True)
        else:
            return print(False)
    except:
        return print(False)


is_date(int(input('Введіть число: ')), int(input('Введіть місяць: ')), int(input('Введіть рік: ')))
