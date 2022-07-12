import datetime
import json
import time
import requests


def get_site_by_requests() -> dict:
    q = input('Введіть місто: ')
    cnt = input('Введіть кількість днів: ')

    link = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=' + q + '&' + 'cnt=' + cnt + '&units=metric&appid=f9ada9efec6a3934dad5f30068fdcbb8'

    return requests.get(link).json()


def site_to_json(j) -> json:
    x = (j["list"])

    with open('temperature.json', 'w') as file:
        json.dump(x, file, indent=2)


def json_decrypt(j_file):
    with open(j_file, 'r+') as f:
        for i in enumerate(json.load(f)):
            date_str = str(datetime.datetime.fromtimestamp(i[1]['dt'])).split()[0]
            print(j_file)



        """for i in enumerate(json.load(f)):
            print(str(datetime.datetime.fromtimestamp("%y-%m-%d", i[1]['dt'])) + ' ' + str(i[1]['temp']['min']) + ' ' + str(i[1]['temp']['max']))"""


site_to_json(get_site_by_requests())
json_decrypt('temperature.json')


