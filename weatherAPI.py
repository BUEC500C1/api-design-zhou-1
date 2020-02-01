import requests
from pprint import pprint

def searchname(cName):
  city = cName
  
  # Not use &units=metric, 404 error
  url = 'https://samples.openweathermap.org/data/2.5/weather?q={}&appid=b6907d289e10d714a6e88b30761fae22'.format(city)

  res = requests.get(url) 
  data = res.json()
  
  temp = data['main']['temp']
  temp_min = data['main']['temp_min']
  temp_max = data['main']['temp_max']
  pressure = data['main']['pressure']
  wind_speed = data['wind']['speed']
  description = data['weather'][0]['description']

  # pprint(data)
  print("Weather in {} is: ".format(city) )
