import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='Онлайн конвертер валют')
    parser.add_argument('-cf', '--currency_from', type=str, default='USD', help='Що конвертуємо')
    parser.add_argument('-ct', '--currency_to', type=str, default='UAH', help='В яку валюту конвертуємо')
    parser.add_argument('-a', '--amount', type=float, default=100.00, help='Кількість')
    parser.add_argument('start_date', type=str, help='Ввести у вигляді: рік-місяць-число')
    parser.add_argument('save_to_file', type=str, help='Зберігаємо у файл?')
    args = parser.parse_args()

    return args


print(parse_args().currency_from)
