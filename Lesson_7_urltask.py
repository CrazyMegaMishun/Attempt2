import argparse
import datetime
import requests
from prettytable import PrettyTable


def get_args():
    parser = argparse.ArgumentParser(description='Онлайн конвертер валют')
    parser.add_argument('cnt', type=str, help='Введіть кількість днів:')
    parser.add_argument('q', type=str, help='Введіть місто:')
    args, unknown = parser.parse_known_args()
    return args


def get_site_by_requests(args) -> dict:
    link = 'http://api.openweathermap.org/data/2.5/forecast/daily?'
    params = {
        'cnt': args.cnt,
        'q': args.q,
        'units': 'metric',
        'appid': 'f9ada9efec6a3934dad5f30068fdcbb8'
    }

    return requests.get(link, params=params).json()


def table_maker(j):
    data = j["list"]
    th = ['Дата', 'Температура вдень', 'Температура вночі']
    td = []
    columns = len(th)
    table = PrettyTable(th)

    for i in enumerate(data):
        td.append(datetime.datetime.fromtimestamp(i[1]['dt']).strftime("%d-%m-%Y"))
        td.append(str(round(i[1]['temp']['day'], 1)) + ' °С')
        td.append(str(round(i[1]['temp']['night'], 1)) + ' °С')

    while td:
        table.add_row(td[:columns])
        td = td[columns:]

    return table


def weather_writer(table, args):
    q = args.q #місто
    cnt = args.cnt #кількість
    day = str(datetime.date.today().strftime("%d-%m-%Y")) #день прогнозу

    with open('{}-{}-{}-days-weather-forecast.txt'.format(day, q, cnt), "w", encoding='utf-8') as file_t:
        file_t.write(str(table))


weather_writer(table_maker(get_site_by_requests(get_args())), get_args())
