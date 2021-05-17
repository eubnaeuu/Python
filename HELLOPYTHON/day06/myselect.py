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

sql = "SELECT * FROM stock WHERE s_code='삼성전자' ORDER BY crawl_date;"
curs.execute(sql)

# result = curs.fetchone():단일행
# result = curs.fetchmany():n행
result = curs.fetchall() # 모든행 

for row in result:
    print(row[2])

conn.close()