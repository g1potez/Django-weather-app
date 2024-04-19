from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

def index(request):
    city = request.GET.get('city')

    if city:
        city = city.lower()
        r = requests.get(f'https://www.ventusky.com/{city}')
        soup = BeautifulSoup(r.text, 'html.parser')

        weatherText = soup.find('td', {'class': 'temperature'}).text
        cityText = soup.find('div', {'class': 'header_background'}).find('h1').text
        nextWeather = soup.find('table', {'class': 'mesto-predpoved'})

        nextWeatherTime = []
        nextWeatherDegress = []
        nextWeatherImg = []

        for time in nextWeather.find('thead').find_all('th'):
            nextWeatherTime.append(time.text)

        for degress in nextWeather.find('tbody').find_all('div', {'class': 'temperature_line'}):
            nextWeatherDegress.append(degress.text)

        for image in nextWeather.find('tbody').find_all('img'):
            nextWeatherImg.append(image['src'])
        
        nextWeatherTime = [item.replace(' tomorrow', '') for item in nextWeatherTime]
        weatherBlock = zip(nextWeatherTime, nextWeatherDegress, nextWeatherImg)
        
        return render(request, 'web/index.html', context={'city': city, 
                                                          'weatherText': weatherText,
                                                          'cityText': cityText,
                                                          'weatherBlock': weatherBlock
                                                          })
    else:
        return render(request, 'web/index.html', context={'city': city})