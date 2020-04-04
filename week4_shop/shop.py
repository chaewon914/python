from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbshop

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('shop.html')

## API 역할을 하는 부분
@app.route('/orders', methods=['POST'])
def write_order():
    name_receive = request.form['name_give']
    count_receive = request.form['count_give']
    address_receive = request.form['address_give']
    number_receive = request.form['number_give']

    db.orders.insert_one({'name':name_receive, 'count':count_receive, 'address':address_receive, 'number':number_receive})

    return jsonify({'result':'success', 'msg': '주문이 성공적으로 완료되었습니다'})


@app.route('/orders', methods=['GET'])
def read_orders():
    orders = list(db.orders.find({},{'_id':0}))
    return jsonify({'result': 'success', 'orders': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)