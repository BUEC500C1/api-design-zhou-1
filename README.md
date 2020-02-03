# Weather-for-Airport-api-design-zhou-1
api-design-zhou-1 created by GitHub Classroom

For all USA Airports, Develop an API and module where we can get current conditions for the airport asked by the API and we can get current weather graphs for specific period

<hr>   

Here, I created three functions in weatherAPI.py, one for searching weather information based on city name, one for getting latitude and longitude information from airport's name based on csv file, last one for searching weather based on latitude and longitude.     

<hr>    

Anyone interested in this project are encouraged to change the name in my two test python files to see the results.    

# Preparation
## Download essential files    
clone my repo:   
```
git clone https://github.com/BUEC500C1/api-design-zhou-1
```

import my function / library to your code    
```
import weatherAPI   
```

## Register an API key of Open Weather     
Click this website https://openweathermap.org/ for more infomation.      
Open my weatherAPI.py, use your API code to replace mine:    
```
url = 'https://samples.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(city, yourAPICode)
```

# Instructions   
Initialize your desired airport place, you can put your desired airport(s) inside this list.       
```
aNames = ["Total Rf Heliport", "Los Angeles County Sheriff's Department Heliport", "Aviosuperficie di Fucecchio", "Darden Airport", "Watson Airport", "Sanya Phoenix International Airport", "Hot Springs Airport"]
```

# Get airport's information    
Once you run my code, you will get below selected weather information for your desired airport.    
```
temp = data['main']['temp']
temp_min = data['main']['temp_min']
temp_max = data['main']['temp_max']
pressure = data['main']['pressure']
wind_speed = data['wind']['speed']
description = data['weather'][0]['description']
```
Results will be written in to "results/results.txt".    

