# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색
import os
import sys
import urllib.request
from bs4 import BeautifulSoup
import pymysql
from bokeh.sphinxext.templates import BJS_CODEPEN_INIT
import datetime



def insertChicken(tuts):
    
    
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

# encText = urllib.parse.quote("치킨")
url = "https://vip.mk.co.kr/newSt/rate/item_all.php"

request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
rescode = response.getcode()

if(rescode==200):
    response_body = response.read()
    # print(response_body.decode('utf-8'))
    soup = BeautifulSoup(response_body,'html.parser')
    itemsTitle = soup.select("td.st2 > a")
    itemsPrice = soup.select("td.st2 + td")
    
    listName = [];
    listCode = [];
    listPrice = [];
    
    for i, item in enumerate(itemsTitle):
        s_name = item.get_text()
        s_code = item.attrs['title']
        listName.append(s_name) 
        listCode.append(s_code)
        
    for idx, item in enumerate(itemsPrice):
        s_price = item.get_text()
        listPrice.append(s_price) 
        
    listans = [];
     
    now = datetime.datetime.now()
    formattedDate = now.strftime("%y%m%d_%H%M")
    print(formattedDate)
    
    for i in range(0,len(listCode)):
        a_name =  listName[i]
        a_code =  listCode[i]
        a_price =  listPrice[i]
        crawl_date = formattedDate 
        
        while((a_price.find(',')) != -1):
            idx = a_price.find(',')
            a_price = a_price[0:idx]+a_price[idx+1:]
            
        listans.append((a_code,a_name,int(a_price),crawl_date))
        
    print(listans)
    
    # cnt = insertChicken(listans)
    # print(cnt)
    
else:
    print("Error Code:" + rescode)
