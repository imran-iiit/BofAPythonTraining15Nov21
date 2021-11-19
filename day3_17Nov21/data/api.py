# csv, excel automation with schedule
# json (Java Script Obj Notation) data - {x:10, name:'murthy'} != Dict = CSV = db data
# api call - json (some old web services even return xml)

# http://api.openweathermap.org/data/2.5/weather?q=chennai&units=imperial&appid=ca3f6d6ca3973a518834983d0b318f73

import requests, json

URL = "http://api.openweathermap.org/data/2.5/weather?q=hyderabad&units=imperial&appid=ca3f6d6ca3973a518834983d0b318f73"

response = requests.get(URL)
print(response.headers)

#if response.headers['Content-Type'] == 'application/json':
report = json.loads(response.text) # convert json to py obj
print(type(report))

desc = report['weather'][0]['description']
print(report['name'], ' weather -------> :', desc)

for i in report:
    if i == 'coord':
        continue

    print(i, '-->', report[i])