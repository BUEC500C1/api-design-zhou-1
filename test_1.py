import pytest
import weatherAPI

def test():
  aNames = ["Total Rf Heliport", "Los Angeles County Sheriff's Department Heliport", "Aviosuperficie di Fucecchio", "Darden Airport", "Watson Airport", "Sanya Phoenix International Airport", "Hot Springs Airport"]
  
  for air in aNames:
    #assert weatherAPI.cityName("London")
    weatherAPI.getdeatiledlocation(air)
