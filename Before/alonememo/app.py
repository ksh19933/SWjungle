from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('mongodb://fefu:evergreen@3.35.14.252', 27017)
db = client.dbjungle

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/memo', methods=['GET'])
def listing():
    # 1. 모든 document 찾기 & _id 값은 출력에서 제외하기
    result = list(db.articles.find({}, {'_id': 0}))
    # 2. articles라는 키 값으로 영화정보 내려주기
    return jsonify({'result':'success', 'articles': result})

## API 역할을 하는 부분
@app.route('/memo', methods=['POST'])
def saving():
		# 1. 클라이언트로부터 데이터를 받기
    url_recieve = request.form['url_give']
    comment_recieve = request.form['comment_give']
		# 2. meta tag를 스크래핑하기
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}
    data = requests.get(url_recieve, headers = headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    url_title = soup.select_one('meta[property="og:title"]')['content']
    url_comment = soup.select_one('meta[property="og:description"]')['content']
    url_image = soup.select_one('meta[property="og:image"]')['content']
		# 3. mongoDB에 데이터 넣기
    doc = {
      'url' : url_recieve,
      'image' : url_image,
      'title' : url_title,
      'desc' : url_comment,
      'comment' : comment_recieve
    }
    db.articles.insert_one(doc)

    return jsonify({'result': 'success', 'msg':'POST 연결되었습니다!'})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)