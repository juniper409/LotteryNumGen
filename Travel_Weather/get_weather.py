import requests
from MAN_HOU import *
appid = '0d74770bc30bbbb88907283c3dbd0800'

def forecast(zip, c_code):
    url = f'https://api.openweathermap.org/data/2.5/weather?zip={zip},{c_code}&units=imperial&appid={appid}'
    response= requests.get(url)
    weather = response.json()
    condition = weather['weather'][0]['main']
    description = weather['weather'][0]['description']
    temp = weather['main']['temp']
    print(description,'',temp,'F')

print('------------ ROUTE FORECASTER ------------')
print("Welcome! Please choose a route:")
print()
print("1. Manchester to Houlton")
print("2. Saco to Houlton")
print("3. Saco to Manchester")
print("4. Manchester to Saco")
print()
select = input("Selection[1-4]:")

if select == 1:
    mtoh()
else:
    print("ERROR")



