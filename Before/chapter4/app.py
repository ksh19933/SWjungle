from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
## URL 별로 함수명이 같거나,
##route의 주소사 같으면 안된다.


@app.route('/')
def home():
   return render_template('index.html')

@app.route('/test', methods=['GET'])
def test_Get():
   title_receive = request.args.get('title_give')
   print(title_receive)
   return jsonify({'result':'success', 'msg':'이 요청은 GET!'})

if __name__ == '__main__':  
   app.run('0.0.0.0', port=5000, debug=True)