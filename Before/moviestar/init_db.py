from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbjungle

from bs4 import BeautifulSoup
import requests

def get_urls():
  headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}
  data = requests.get('https://movie.naver.com/movie/sdb/rank/rpeople.naver', headers = headers)
  soup = BeautifulSoup(data.text,'html.parser')
  trs = soup.select('#old_content > table > tbody > tr')

  urls = []
  for tr in trs:
    a = tr.select_one('td.title > a')
    if a is not None:
      base_url = 'https://movie.naver.com/'
      url = base_url + a['href']
      urls.append(url)

  return urls




def insert_star(url):
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}
    data = requests.get(url, headers = headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    name = soup.select_one('#content > div.article > div.mv_info_area > div.mv_info.character > h3 > a').text
    recent_work = soup.select_one('#content > div.article > div.mv_info_area > div.mv_info.character > dl > dd > a:nth-child(1)').text
    img_url = soup.select_one('#content > div.article > div.mv_info_area > div.poster > img')['src']
    #content > div.article > div.mv_info_area > div.mv_info.character > dl > dd:nth-child(4)
    doc ={
      'url' : url,
      'name' : name,
      'recent' : recent_work,
      'img_url' : img_url,
      'like' : 0
    }
    db.mystar.insert_one(doc)

def insert_all():
  db.mystar.drop()
  urls = get_urls()
  for url in urls:
    insert_star(url)

insert_all()