import argparse
import json
from datetime import datetime, timedelta, date
import requests
from tabulate import tabulate

parser = argparse.ArgumentParser(description='Онлайн конвертер валют')
parser.add_argument('cf', type=str, default='USD', help='Що конвертуємо')
parser.add_argument('ct', type=str, default='UAH', help='В яку валюту конвертуємо')
parser.add_argument('a', type=float, default=100.00, help='Кількість')
parser.add_argument('-sd', '--start_date', type=str, default=str(date.today()), help='Дата (рік-місяць-день)')
parser.add_argument('-save', '--save_to_file', type=str, help='Зберігаємо у файл (Y/N)?')
args, unknown = parser.parse_known_args()


def date_check(d) -> str:
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


def get_site_by_requests(i) -> json:
    link = 'https://api.exchangerate.host/convert?'
    c1 = 'from=' + currency_check(args.cf) + '&'
    c2 = 'to=' + currency_check(args.ct) + '&'
    number = 'amount=' + str(args.a) + '&'
    d1 = 'date=' + str(datetime.strptime(date_check(args.save_to_file), "%Y-%m-%d") - timedelta(days=i)).split()[0]

    link = link + c1 + c2 + number + d1

    with open('exchange_rates.json', 'w') as f:
        json.dump(requests.get(link).json(), f, indent=2)


def json_to_list() -> list:
    with open('exchange_rates.json', 'r') as f:
        content = json.loads(f.read())
        x = [content['date'],
             content['query']['from'],
             content['query']['to'],
             content['query']['amount'],
             content['info']['rate'],
             content['result']]

    return x


def exchange_rate_writer():
    headers = ['date', 'from', 'to', 'amount', 'rate', 'result']
    contents = []

    for i in range(5):
        get_site_by_requests(i)
        contents.append(json_to_list())

    table = tabulate(contents, headers=headers, tablefmt='pipe', stralign='center')

    if args.save_to_file == 'N':
        print(table)
    elif args.save_to_file == 'Y':
        with open('exchange_rates.txt', 'w') as f:
            f.write(table)


exchange_rate_writer()
