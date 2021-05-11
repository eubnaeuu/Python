import pymysql

conn = pymysql.connect(
    user='root', 
    passwd='java', 
    host='127.0.0.1', 
    db='python', 
    charset='utf8'
)

# curs = conn.cursors()  #에러남
curs = conn.cursor(pymysql.cursors.DictCursor) #컬럼명O
curs = conn.cursor() # 컬럼명 X

sql = "SELECT col01, col02, col03 FROM hello;"
curs.execute(sql)

# result = curs.fetchone():단일행
# result = curs.fetchmany():n행
result = curs.fetchall() # 모든행 

for row in result:
    print(row[0])
