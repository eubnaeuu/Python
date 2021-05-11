import pymysql

conn = pymysql.connect(
    user='root', 
    passwd='java', 
    host='127.0.0.1', 
    db='python', 
    charset='utf8'
)

# 단일입력
curs = conn.cursor(pymysql.cursors.DictCursor)
sql = "INSERT INTO HELLO(col01, col02, col03) VALUES(1,'2','3');"
cnt = curs.execute(sql)
print("cnt : ", cnt)
conn.commit()
conn.close()


# 다중입력
tuts = (
    ('1','1','1'),
    ('2','2','2'),
    ('3','3','3')
    )
curs = conn.cursor(pymysql.cursors.DictCursor)
sql = "INSERT INTO HELLO(col01, col02, col03) VALUES(%s,%s,%s);"
cnt = curs.executemany(sql,tuts)
print("cnt : ", cnt)
conn.commit()
conn.close()