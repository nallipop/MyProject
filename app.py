from flask import Flask, render_template, request, jsonify
from pymongo import  MongoClient

app=Flask(__name__)

client=MongoClient('localhost', 27017)
db=client.dbsparta



@app.route('/')
def home():
    return render_template('index.html')

##아래는 api역할을 하는 부분
@app.route('/menu', methods=['post'])
def add_menu():
    # 1. 클라이언트가 준 title, author, review 가져오기.
    # post 라는 자료 방식에서는 아래의 request.form 이라는 형태로 씀

    #title_receive로 클라이언트가 준 title 가져오기
    img_receive = request.form['img_give']
    name_receive = request.form['name_give']
    text_receive = request.form['text_give']
    price_receive = request.form['price_give']

#아래는 DB에 삽입할 menuList 만들기
    menu={
        'img':img_receive
        'name':name_receive,
        'text':text_receive,
        'price':price_receive

    }
    # 2. DB에 정보 삽입하기
    db.menus.insert_one(menu)

#성공 여부와 성공시 메시지 반환
    return jsonify({'result':'success', 'msg':'메뉴추가가 완료되었습니다.'})


@app.route('/menu', methods=['get'])
def read_menus():
    # 1. DB에서 리뷰 정보 모두 가져오기 (근데 id 는 필요없어요  가 0 ㅇ의미)
    menus=list(db.menus.find({}, {'_id':0}))
    #1. 모든 메뉴s의 데이터를 가지고 온 후 list로 변환한다
    #2. 성공 메세지와 함께 리뷰를 내보낸다
    # return jsonify({'result':'success', 'msg':'메뉴를 성공적으로 받아왔다!! 아오!!'})
    return jsonify({'result':'success', 'reviews':menus})

if __name__=='__main__':
    app.run('0.0.0.0', port=5000, debug=True)