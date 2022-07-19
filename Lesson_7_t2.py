#Завдання 2
temperature = float(input('Введіть температуру: '))
temperature_type = input('Введіть тип температури(C - Цельсій, F - Фаренгейт, K - Кельвін): ')


def get_celsius(t_num, t_type):
    match t_type:
        case 'C':
            return t_num
        case 'F':
            return (t_num*(9/5)) + 32
        case 'K':
            return t_num + 273.15


def get_fahrenheit(t_num, t_type):
    match t_type:
        case 'C':
            return (t_num-32) * (5/9)
        case 'F':
            return t_num
        case 'K':
            return ((t_num-32) * (5/9)) + 273.15


def get_kelvin(t_num, t_type):
    match t_type:
        case 'C':
            return t_num - 273.15
        case 'F':
            return (t_num - 273.15) * (9/5) + 32
        case 'K':
            return t_num


print('У цельсіях: ' + str(get_celsius()))
print('У фаренгейтах:' + str(get_fahrenheit()))
print('У кельвінах: ' + str(get_kelvin()))
