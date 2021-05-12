import pymysql

def insertStock(tuts):
    conn = pymysql.connect(
        user='root', 
        passwd='java', 
        host='127.0.0.1', 
        db='python', 
        charset='utf8'
    )
    curs = conn.cursor()
    sql = "INSERT INTO stock(s_code, s_name, s_price, crawl_date) VALUES(%s,%s,%s,%s);"
    cnt = curs.executemany(sql,tuts)
    conn.commit()
    conn.close()    
    return cnt