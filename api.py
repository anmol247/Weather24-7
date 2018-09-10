import requests

api_key = 'f71faf0812d1c1e500fa0748335a2346'
city = input('Enter a city: ')
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'.format(city, api_key)
res = requests.get(url).json()

# it's 28c in chennai
temp = res['main']['temp']
print("It's {} Celcius in {}".format(temp, city.title()))
