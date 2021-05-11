# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색
import os
import sys
import urllib.request
from bs4 import BeautifulSoup
import pymysql

def insertChicken(tuts):
    conn = pymysql.connect(
        user='root', 
        passwd='java', 
        host='127.0.0.1', 
        db='python', 
        charset='utf8'
    )
    
    curs = conn.cursor()
    sql = "INSERT INTO chicken(title, description, link, bloggername, bloggerlink, postdate) VALUES(%s,%s,%s,%s,%s,%s);"
    cnt = curs.executemany(sql,tuts)
    conn.commit()
    conn.close()    
    return cnt

client_id = "t6LiD84QhVfZT1L1rFXg"
client_secret = "LH_y_XvemI"
encText = urllib.parse.quote("치킨")
urlxml = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(urlxml)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()

if(rescode==200):
    response_body = response.read()
    # print(response_body.decode('utf-8'))
    xmlsoup = BeautifulSoup(response_body,'xml')
    # print(xmlsoup)
    items = xmlsoup.select("item")
    tuts = []
    for idx, item in enumerate(items):
        title       = item.title.getText()
        description = item.description.getText()
        link         = item.link.getText()
        bloggername = item.bloggername.getText()
        bloggerlink = item.bloggerlink.getText()
        postdate     = item.postdate.getText()
        tuts.append((title,description,link,bloggername,bloggerlink,postdate))
    cnt = insertChicken(tuts)
    print(cnt)
else:
    print("Error Code:" + rescode)

     
   
    