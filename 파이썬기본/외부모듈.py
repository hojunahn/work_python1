# from simple_colors import *
#
# print(red('hello'))
# print(green('hello', 'bold'))
# print(blue('hello', ['bold', 'underlined']))

import requests
from bs4 import BeautifulSoup
url = "https://www.weather.go.kr/weather/observation/currentweather.jsp"
html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")
print(soup)