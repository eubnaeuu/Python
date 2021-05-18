from flask import Flask
from flask.globals import request
from flask.json import jsonify
from flask.templating import render_template
from day11 import mydao_exam
from day11.mydao_exam import DaoExam
app = Flask(__name__, static_url_path="") # static 경로 설정



de = DaoExam()


@app.route('/')
@app.route('/list')
def list():
    mylist = de.myselect()
    return render_template('examlist.html',mylist=mylist)

@app.route('/add.ajax', methods=['POST'])
def ajax_add():
    p = request.get_json()
    e_id = p['e_id']   # p.e_id (X)  p['e_id'] (O)  p.get("e_id",None) (O)
    kor = p['kor']
    eng = p['eng']
    math = p['math']
    
    print("e_id:{} kor:{} eng:{} math:{}".format(e_id, kor, eng, math))
    cnt = de.myinsert(e_id, kor, eng, math)
    
    if cnt == 1:
        msg = "ok"
    else:
        msg = "ng"
    
    return jsonify(msg = msg)

@app.route('/upd.ajax', methods=['POST'])
def ajax_update():
    print("ajax_update 들어옴")
    p = request.get_json()
    print(p)
    e_id = p['e_id']
    kor = p['kor']
    eng = p['eng']
    math = p['math']
    
    cnt = de.myupdate(e_id, kor, eng, math)
    
    if cnt == 1:
        msg = "ok"
    else:
        msg = "ng"
    
    return jsonify(msg = msg)

@app.route('/del.ajax', methods=['POST'])
def ajax_delete():
    p = request.get_json()
    e_id = p['e_id']  
    
    cnt = de.mydelete(e_id)
    
    if cnt == 1:
        msg = "ok"
    else:
        msg = "ng"
    
    return jsonify(msg = msg)

if __name__ == '__main__':
    app.run(debug=True)