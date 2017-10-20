import urlib.parse
import requests
import weather

main_api= 'https://ca.news.yahoo.com/weather/canada/'

while True:
  place = input('place: ')
   if location == 'quit' or place = 'q':
     break
  url = main_api + urlib.parse.urlencode({'location:location'})
  print(url)
  json_data = requests.get(url).json()
  
