import requests
from bs4 import BeautifulSoup
import datetime

now = datetime.datetime.now().strftime('%Y.%m.%d.%H:00')

def get_weather_info():
  url = 'https://www.weather.go.kr/weather/observation/currentweather.jsp?tm=' + now + '&type=t99&mode=0&reg=100&auto_man=m&stn=108'
  headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}
  data = requests.get(url, headers=headers)
  soup = BeautifulSoup(data.text, 'html.parser')
  current_weather = soup.select('#content_weather > table > tbody > tr:nth-child(1) >td')

  temp = current_weather[5].text
  wind_chill = current_weather[7].text
  moisture = current_weather[9].text
  wind_dir = current_weather[10].text
  wind_speed = current_weather[11].string.split("'")[1]

  info_doc = {
    "temp" : temp,
    "wind_chill" : wind_chill,
    "moisture" : moisture,
    "wind_dir" : wind_dir,
    "wind_speed" : wind_speed
  }
  return info_doc