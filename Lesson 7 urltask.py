import json
import requests
from urllib import request
from http.client import HTTPResponse


def get_site():
    return request.urlopen('http://api.openweathermap.org/data/2.5/forecast/daily?q=city&cnt=1&units=metric&appid=f9ada9efec6a3934dad5f30068fdcbb8')


def get_site_by_requests() -> HTTPResponse:
    return requests.get('http://api.openweathermap.org/data/2.5/forecast/daily?q=city&cnt=1&units=metric&appid=f9ada9efec6a3934dad5f30068fdcbb8', params='city')


print(get_site_by_requests())

