#Завдання 1
coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
code = ('BTC', 'ETH', 'XRP', 'LTC')


def dict_maker(keys, values):
    x = {}

    for i in range(len(keys)):
        x[keys[i]] = values[i]

    return x


print(dict_maker(coin, code))


# Завдання 2
import json
import time


def get_tracks_time(file):
    seconds = 0

    with open(file, 'r') as f:
        for i in enumerate(json.load(f)['album']['tracks']['track']):
            seconds += (int(i[1]['duration']))

    return seconds


def get_general_time(x):
    return time.strftime("%H:%M:%S", time.gmtime(x))


print(get_general_time(get_tracks_time('acdc.json')))


#Завдання 3
a = ['a', 'b', 'c', 'd', 'e']


def get_list_to_dict(x):
    d = dict.fromkeys(i for i in range(len(x)))
    for i in d:
        d[i] = x[i]

    return d


print(get_list_to_dict(a))


#Завдання 4

import time
from datetime import datetime


def what_time_is_it_now():
    dt = datetime.now()

    for i in range(1, 4):
        time.sleep(1)
        print(i)

    return dt.strftime('%H:%M')


print(what_time_is_it_now())
