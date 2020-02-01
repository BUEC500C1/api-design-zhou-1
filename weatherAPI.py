import requests

city = input('Enter your city name: ')

url = 'https://samples.openweathermap.org/data/2.5/weather?q={}&appid=b6907d289e10d714a6e88b30761fae22'.format(city)

res = requests.get(url)

print(res)
