import datetime
import urllib.request
from bs4 import BeautifulSoup
import pymysql
import time


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

for i in range(10):
    url = "https://vip.mk.co.kr/newSt/rate/item_all.php"
    
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    
    if(rescode==200):
        response_body = response.read()
        html = response_body.decode('euc-kr')
        soup = BeautifulSoup(html,'html.parser')
        
        items = soup.select("td.st2")
        
        now = datetime.datetime.now()
        formattedDate = now.strftime("%y%m%d_%H%M")
        
        stockList = [];
        
        for i, item in enumerate(items):
            s_name = item.text
            s_code = item.a.attrs['title']
            s_price = item.parent.select('td')[1].text.replace(",","")
            
            stockList.append((s_name, s_code, s_price, formattedDate))
            
        cnt = insertStock(stockList)
        print(cnt)
        
    else:
        print("Error Code:" + rescode)

    time.sleep(60)