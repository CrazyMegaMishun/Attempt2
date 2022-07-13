import datetime
import json
import requests
from prettytable import PrettyTable


def get_site_by_requests() -> dict:
    q = input('Введіть місто: ')
    cnt = input('Введіть кількість днів: ')

    link = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=' + q + '&' + \
           'cnt=' + cnt + '&units=metric&appid=f9ada9efec6a3934dad5f30068fdcbb8'

    return requests.get(link).json()


def site_to_json(j):
    x = j["list"]
    q = str(j["city"]["name"])
    cnt = str(j["cnt"])
    d = str(datetime.datetime.fromtimestamp(x[0]["dt"]).strftime("%d-%m-%Y"))

    th = ['Дата', 'Температура вдень', 'Температура вночі']
    td = []
    columns = len(th)
    table = PrettyTable(th)

    for i in enumerate(x):
        td.append(datetime.datetime.fromtimestamp(i[1]['dt']).strftime("%d-%m-%Y"))
        td.append(str(round(i[1]['temp']['day'], 1)) + ' °С')
        td.append(str(round(i[1]['temp']['night'], 1)) + ' °С')

    td_data = td[:]

    while td_data:
        table.add_row(td_data[:columns])
        td_data = td_data[columns:]


    with open(d+'-'+q+'-'+cnt+'-days-weather-forecast.txt', "w", encoding='utf-8') as file_t:
        file_t.write(str(table))
        """file_t.write('Дата Температура вдень Температура вночі' + '\n')
        for i in enumerate(x):
            file_t.write(datetime.datetime.fromtimestamp(i[1]['dt']).strftime("%d-%m-%Y") + ' '
                         + str(i[1]['temp']['day']) + ' ' + str(i[1]['temp']['night']) + '\n')"""



site_to_json(get_site_by_requests())

