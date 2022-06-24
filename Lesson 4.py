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
"""
#Завдання 7
list_1 = int(input())
list_2 = int(input())


def list_maker(x):
    y = list()
    while x > 0:
        y.append(x % 10)
        x = (x - (x % 10)) // 10
    return y


def search_common(): #общие для двух
    pass


def get_unique_first(): #есть в первом, но нет во втором
    pass


def get_unique_both(): #уникальные для обоих
    pass


print(search_common())
print(get_unique_first())
print(get_unique_both())
