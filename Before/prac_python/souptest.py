import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20200303', headers = headers)

soup = BeautifulSoup(data.text, 'html.parser')

movies = soup.select('#old_content > table > tbody > tr')
print(len(movies))

for movie in movies:
  a_rank = movie.select_one('td.ac > img')
  a_tag = movie.select_one('td.title > div > a').text
  a_point = movie.select_one('td.point').text
  if a_tag != None:
    print(a_rank['alt'], a_tag, a_point)



# old_content > table > tbody > tr:nth-child(2) > td:nth-child(1) > img
# old_content > table > tbody > tr:nth-child(3) > td.title > div > a
# old_content > table > tbody > tr:nth-child(3) > td.point

