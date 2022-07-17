import argparse
import json
from datetime import datetime, timedelta, date
import requests

parser = argparse.ArgumentParser(description='Онлайн конвертер валют')
parser.add_argument('-cf', '--currency_from', type=str, default='USD', help='Що конвертуємо')
parser.add_argument('-ct', '--currency_to', type=str, default='UAH', help='В яку валюту конвертуємо')
parser.add_argument('-a', '--amount', type=float, default=100.00, help='Кількість')
parser.add_argument('-sd', '--start_date', type=str, default=str(date.today()), help='Дата')
parser.add_argument('-save', '--save_to_file', type=str, help='Зберігаємо у файл?')
args, unknown = parser.parse_known_args()


def date_check(d) -> date:
    try:
        if datetime.strptime(d, "%Y-%m-%d") - timedelta(days=1) >= datetime.today():
            return str(date.today()).split()[0]
        else:
            return d
    except ValueError:
        return str(date.today()).split()[0]


def currency_check(currency) -> str:
    with open('symbols.json', 'r') as f:
        if currency in json.load(f)['symbols']:
            return currency
        else:
            return ''


def get_site_by_requests(i):
    link = 'https://api.exchangerate.host/convert?'
    c1 = 'from=' + currency_check(args.currency_from) + '&'
    c2 = 'to=' + currency_check(args.currency_to) + '&'
    number = 'amount=' + str(args.amount) + '&'
    d1 = 'date=' + str(datetime.strptime(date_check(args.start_date), "%Y-%m-%d") - timedelta(days=i)).split()[0]

    link = link + c1 + c2 + number + d1

    with open('exchange_rates.json', 'w') as f:
        json.dump(requests.get(link).json(), f, indent=2)


def json_to_txt():
    x = [['date', 'from', 'to', 'amount', 'rate', 'result']]
    y = list()

    with open('exchange_rates.json', 'r') as f:
        for i in json.load(f).items():
            y.append(i)

        for i in enumerate(y):
            x.append([y[5]['date'], y[2]['query']['from'], y[2]['query']['to'], y[2]['query']['amount']])


    #with open('exchange_rates.txt', 'w') as f:

def exchange_rate_writer():
    for i in range(5):
        get_site_by_requests(i)
        json_to_txt()


exchange_rate_writer()
