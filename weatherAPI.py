import requests
import csv
from pprint import pprint

# test use
def searchname(cName):
  city = cName
  
  file1 = open("results/results.txt","w") 
  
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
  # print("Weather in {} is: ".format(city) )
  file1.write("temp there is {} \n".format(temp) )
  file1.write("Min temp there is {} \n".format(temp_min) )
  file1.write("Max temp there is {} \n".format(temp_max) )
  file1.write("Pressure there is {} \n".format(pressure) )
  file1.write("Speed of wind there is {} \n".format(wind_speed) )
  file1.write("Description of weather there is {} \n".format(description) )
  
  file1.close()

  
  
# def for get lati and longi from airport's name
def getdeatiledlocation(aName):
  airportName = aName
  file2 = "csvFiles/airport-codes_csv.csv"
  
  with open(file2) as csv_file:
    csvitem = list(csv.reader(csv_file) )
    
    for row in csvitem:
      if row[3] == airportName:
        lati = row[4]
        longi = row[5]
        # print(lati, longi)
        searchdimension(lati, longi)  
            

# search based on lati and longi
def searchdimension(lati, longi):
  latitude = lati
  longitude = longi
  
  file1 = open("results/results.txt","a+") 
  
  # Not use &units=metric, 404 error
  url = 'https://samples.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid=b6907d289e10d714a6e88b30761fae22'.format(latitude, longitude)

  res = requests.get(url) 
  data = res.json()
  
  temp = data['main']['temp']
  temp_min = data['main']['temp_min']
  temp_max = data['main']['temp_max']
  pressure = data['main']['pressure']
  wind_speed = data['wind']['speed']
  description = data['weather'][0]['description']

  file1.write("temp there is {} \n".format(temp) )
  file1.write("Min temp there is {} \n".format(temp_min) )
  file1.write("Max temp there is {} \n".format(temp_max) )
  file1.write("Pressure there is {} \n".format(pressure) )
  file1.write("Speed of wind there is {} \n".format(wind_speed) )
  file1.write("Description of weather there is {} \n".format(description) )
  
  file1.close()

  # print out result
  f = open("results/results.txt","r")
  print(f.read() )
  f.close()
  
  
  
  
  
