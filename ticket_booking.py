# coding=utf-8
from flask import render_template
from flask import Flask
import MySQLdb
from flask import request

app = Flask(__name__)

@app.route('/xq')
def hello_world():
    return render_template('xq.html')
  
@app.route('/')
def wenlx():
    return render_template('wenlx.html')

@app.route('/jn')
def jn():
    return render_template('jn.html')

@app.route('/xm')
def xm():
    return render_template('xm.html')


@app.route('/about')
def about():
    return render_template('aboutme.html')

@app.route('/tb')
def tb():
    conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='',db='ticket_booking',port=3306)
    cur=conn.cursor()
    count = cur.execute('select * from tickets')
    t = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('tb.html', tickets=t)

@app.route('/gm', methods=['GET'])
def gm():
    name = request.args.get('name', '')
    id_card = request.args.get('id_card', '')
    id_ticket = request.args.get('id_ticket', '')
    print name,id_card,id_ticket
    # 插入数据
    conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='',db='ticket_booking',port=3306)
    cur=conn.cursor()
    sql = "insert into user(user_name,id_card,ticket_id) values('%s','%s','%s')" % (name,id_card,id_ticket)
    print sql
    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()
    

    # 从数据库获取数据
    conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='',db='ticket_booking',port=3306)
    cur=conn.cursor()
    count = cur.execute('select * from user')
    u = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('gm.html', users=u)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
