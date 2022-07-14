import argparse
from datetime import date
import requests


def get_site_by_requests() -> dict:
    parser = argparse.ArgumentParser(description='Онлайн конвертер валют')
    parser.add_argument('-cf', '--currency_from', type=str, default='USD', help='Що конвертуємо')
    parser.add_argument('-ct', '--currency_to', type=str, default='UAH', help='В яку валюту конвертуємо')
    parser.add_argument('-a', '--amount', type=float, default=100.00, help='Кількість')
    parser.add_argument('-sd', '--start_date', type=str, default=str(date.today()), help='Дата')
    parser.add_argument('-save', '--save_to_file', type=str, help='Зберігаємо у файл?')
    args, unknown = parser.parse_known_args()

    link = 'https://api.exchangerate.host/convert?'
    c1 = 'from=' + args.currency_from + '&'
    c2 = 'to=' + args.currency_to + '&'
    number = 'amount=' + str(args.amount) + '&'
    d = 'd=' + args.start_date

    return requests.get(link + c1 + c2 + number + d).json()


print(get_site_by_requests())
