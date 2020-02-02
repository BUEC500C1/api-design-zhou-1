# test case for search weather information based on city names

import pytest
import weatherAPI

def test():
  cityNames = ["London", "Beijing", "New York", "Tokyo", "Hangzhou", "Boston", "Seattle"]
  
  for a in cityNames:
    #assert weatherAPI.cityName("London")
    weatherAPI.searchname(a)
