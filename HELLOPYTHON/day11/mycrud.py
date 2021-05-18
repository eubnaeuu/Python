from flask import Flask
from flask.globals import request
from flask.json import jsonify
from flask.templating import render_template
from day11 import mydao_emp
from day11.mydao_emp import DaoEmp
app = Flask(__name__, static_url_path="") # static 경로 설정
de = DaoEmp()
@app.route('/')
@app.route('/list')
def list():
    mylist = de.myselect()
    return render_template('list.html',mylist=mylist)

@app.route('/add.ajax', methods=['POST'])
def ajax_add():
    p = request.get_json()
    e_id = p['e_id']   # p.e_id (X)  p['e_id'] (O)  p.get("e_id",None) (O)
    e_name = p['e_name']
    birth = p['birth']
    
    print("e_id:{} e_name:{} birth:{}".format(e_id, e_name, birth))
    cnt = de.myinsert(e_id, e_name, birth)
    
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
    e_name = p['e_name']
    birth = p['birth']
    
    cnt = de.myupdate(e_id, e_name, birth)
    
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