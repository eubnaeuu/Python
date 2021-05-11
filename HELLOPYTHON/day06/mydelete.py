import pymysql

conn = pymysql.connect(
    user='root', 
    passwd='java', 
    host='127.0.0.1', 
    db='python', 
    charset='utf8'
)

curs = conn.cursor(pymysql.cursors.DictCursor)
sql = "DELETE FROM hello WHERE col01 = 3;"
cnt = curs.execute(sql)
print("cnt : ", cnt)
conn.commit()
conn.close()