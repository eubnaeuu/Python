import pymysql

conn = pymysql.connect(
    user='root', 
    passwd='java', 
    host='127.0.0.1', 
    db='python', 
    charset='utf8'
)

curs = conn.cursor(pymysql.cursors.DictCursor)

sql = """
        UPDATE hello 
        SET 
        col02='5'
        ,col03='2' 
        WHERE col01 = 4;
    """
cnt = curs.execute(sql)
print("cnt : ", cnt)
conn.commit()
conn.close()