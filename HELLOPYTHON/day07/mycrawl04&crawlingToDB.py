# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색
import os
import sys
import urllib.request
from bs4 import BeautifulSoup
import pymysql
from bokeh.sphinxext.templates import BJS_CODEPEN_INIT

def insertChicken(tuts):
    conn = pymysql.connect(
        user='root', 
        passwd='java', 
        host='127.0.0.1', 
        db='python', 
        charset='utf8'
    )
    curs = conn.cursor()
    sql = "INSERT INTO stock(s_code, s_name, s_price, crawl_date) VALUES(%s,%s,%s,DATE_FORMAT(now(), '%y%m%d %h:%m'));"
    cnt = curs.executemany(sql,tuts)
    conn.commit()
    conn.close()    
    return cnt

client_id = "t6LiD84QhVfZT1L1rFXg"
client_secret = "LH_y_XvemI"
# encText = urllib.parse.quote("치킨")
url = "https://vip.mk.co.kr/newSt/rate/item_all.php"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()

if(rescode==200):
    response_body = response.read()
    # print(response_body.decode('utf-8'))
    soup = BeautifulSoup(response_body,'html.parser')
    itemsTitle = soup.select("td.st2 > a")
    itemsPrice = soup.select("td.st2 + td")
    # tuts = []
    listName = [];
    listCode = [];
    listPrice = [];
    # for idx, item in enumerate(itemsTotal):
    #     s_tmp = item
    #     print(item)
    #
    
    for idx, item in enumerate(itemsTitle):
        s_name = item.get_text()
        s_code = item.attrs['title']
        listName.append(s_name) 
        listCode.append(s_code)
        # print("item : ",item)
        # print("name : ",s_name)
        # print("code : ",s_code)
        # print(item.title.get_Text())
    for idx, item in enumerate(itemsPrice):
        s_price = item.get_text()
        listPrice.append(s_price) 
        # print("price : ",s_price)
        # title       = item.title.getText()
        # tuts.append((title,description,link,bloggername,bloggerlink,postdate))
    listans = []; 
#     >> while treeHit < 10:
# ...     treeHit = treeHit +1
# ...     print("나무를 %d번 찍었습니다." % treeHit)
# ...     if treeHit == 10:

    for i in range(0,len(listCode)):
        a_name =  listName[i]
        a_code =  listCode[i]
        a_price =  listPrice[i]
        while(listPrice[i].find(',') != -1):
            idx = listPrice[i].find(',')
            a_price = int(a_price[0:idx]+a_price[idx+1:])
            print(a_price)
            listans.append((a_name,a_code,a_price))
        
    # cnt = insertChicken(listans)
else:
    print("Error Code:" + rescode)
