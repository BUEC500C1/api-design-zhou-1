<strong>Weather.gov API</strong>        
https://www.weather.gov/documentation/services-web-api     
The API uses the request headers to modify the response returned: Request new features, Format the response...     
No API key buy a User Agent string is required to identify application. (unique for security)     
API location: https://api.weather.gov/    
Endpoints typically have a GeoJSON default format, given the inclusion of geometry data.     
GeoJSON: application/geo+json      
For example, to discover the endpoint of the raw forecast, the application would first request:    
https://api.weather.gov/points/39.7456,-97.0892     
This response tells the application where to find relative information–including office, zone and forecast data–for a given point. The application can then use the linked data in the previous response to locate the raw forecast:     
https://api.weather.gov/gridpoints/TOP/31,80     


<strong>OpenWeatherMAP API</strong>        
https://openweathermap.org/api    
