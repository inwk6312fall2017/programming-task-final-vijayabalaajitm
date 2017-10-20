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
  
  json_status = json_data['status']
  print('API status: '+ jason_status)  
  
  if json_status == 'OK':
    for each in jason_data['resultsaformatted_place = json_data['results'][4]['formatted_location'] "My logic is to print the first five results, by getting the first five values using the list"
    print()
    print(formatted_place)
