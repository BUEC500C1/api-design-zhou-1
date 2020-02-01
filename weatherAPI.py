import requests
from pprint import pprint

def searchname(cName):
  city = cName
  
  url = 'https://samples.openweathermap.org/data/2.5/weather?q={}&appid=b6907d289e10d714a6e88b30761fae22&units=metric'.format(city)

  res = requests.get(url) 
  data = res.json()
  
  temp = data["main"]["temp"]

  # pprint(data)
  print("Weather in {} is: ".format(city) )
