#Завдання 2
temperature = float(input('Введіть температуру: '))
temperature_type = input('Введіть тип температури(C - Цельсій, F - Фаренгейт, K - Кельвін): ')


def get_celsius(t_num, t_type):
    temps = {
        'C': t_num,
        'F': round((t_num*(9/5)) + 32, 1),
        'K': round(t_num + 273.15, 2)
    }
    return temps[t_type]


def get_fahrenheit(t_num, t_type):
    temps = {
        'C': round((t_num-32) * (5/9), 2),
        'F': t_num,
        'K': round((t_num-32) * (5/9) + 273.15, 2)
    }
    return temps[t_type]


def get_kelvin(t_num, t_type):
    temps = {
        'C': round(t_num - 273.15, 2),
        'F': round((t_num - 273.15) * (9/5) + 32, 1),
        'K': t_num
    }
    return temps[t_type]


print('У цельсіях: ' + str(get_celsius(temperature, temperature_type)))
print('У фаренгейтах: ' + str(get_fahrenheit(temperature, temperature_type)))
print('У кельвінах: ' + str(get_kelvin(temperature, temperature_type)))
