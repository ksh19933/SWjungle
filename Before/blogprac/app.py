import datetime
now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
import static.weather as info
weather_info = info.get_weather_info()

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbmyblog
from flask import Flask, request, render_template, jsonify

def ObjectIdToJson(db_data):
  db_data['_id'] = str(db_data['_id'])
  return db_data

app = Flask(__name__)
if __name__ == '__main__':
  app.run('0.0.0.0', port=5000, debug=True)

@app.route('/')
def home():
  return render_template('index.html')


@app.route('/data', methods = ['GET'])
def get_index_data():
  result = list(db.post.find({}, {'_id':False}))
  return jsonify({'result':'success','post_list':result, 'weather_info':weather_info, 'posted_data': now})


@app.route('/page', methods = ['GET'], strict_slashes = False)
def get_postpage():
  key = request.args.get('date')
  if key != None:
    db_data = db.post.find_one({'posted_date':key})
    # db_data['_id'] = str(db_data['_id'])
    print(db_data)
    return render_template('postpage.html', db_data = db_data)
  else:
    return render_template('postpage.html', db_data = None)

@app.route('/page', methods = ['POST'])
def save_page():
  key = request.args.get('date')
  print(key)
  title_receive = request.form['title_give']
  text_receive = request.form['text_give']
  category_receive = request.form['category_give']
  doc = {
    'title' : title_receive,
    'text' : text_receive,
    'category' : category_receive,
    'posted_date' : now,
  }
  db.post.insert_one(doc)
  return jsonify({'result':'success'})

@app.route('/page/update', methods = ['POST'])  
def update_page():
  print("update_start")
  title_receive = request.form['title_give']
  text_receive = request.form['text_give']
  category_receive = request.form['category_give']
  key = request.form['posted_date']
  db.post.update_one({'posted_date':key, 'title':title_receive}, 
  {'$set': {
      'title' : title_receive,
      'text' : text_receive,
      'category' : category_receive, 
      }
  })
  return jsonify({'result':'success'})

@app.route('/page/delete', methods =['POST'])
def remove():
  title_receive = request.form['title_give']
  key = request.form['posted_date']
  db.post.remove({'posted_date':key,'title': title_receive})
  return jsonify({'result':'success'})

if __name__ == '__main__':
  app.run('0.0.0.0', port=5000, debug=True)


