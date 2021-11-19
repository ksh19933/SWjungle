from flask import Flask, request, render_template, jsonify
from pymongo import MongoClient
from  bson import ObjectId


client = MongoClient('mongodb://fefu:fefu2@52.79.241.187',27017)
db = client.dbmemo

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/', methods = ['POST'])
def create():
  title_receive = request.form['title_give']
  text_receive = request.form['text_give']
  doc = {
    'title':title_receive,
    'text': text_receive,
  }
  db.memocard.insert_one(doc)
  return jsonify({'result':'success'})

@app.route('/data', methods =['GET'])
def read():
  datas = list(db.memocard.find({}))
  db_data = []
  for data in datas:
    data['_id'] = str(data['_id'])
    db_data.append(data)
  return jsonify({'result':'success', 'db_data':db_data})

@app.route('/update', methods=['POST'])
def update():
  _id = request.form['_id']
  id = ObjectId(_id)
  title_receive = request.form['title_give']
  text_receive = request.form['text_give']
  db.memocard.update_one({'_id': id},{'$set':{'title':title_receive, 'text':text_receive}})
  return jsonify({'result':'success'})

@app.route('/delete', methods=['POST'])
def delete():
  _id = request.form['_id']
  id = ObjectId(_id)
  db.memocard.delete_one({'_id': id})
  return jsonify({'result':'success'})




if __name__ == '__main__':
  app.run('0.0.0.0', port=5000, debug=True)