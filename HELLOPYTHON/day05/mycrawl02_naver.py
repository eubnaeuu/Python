# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색
import os
import sys
import urllib.request
from bs4 import BeautifulSoup
client_id = "t6LiD84QhVfZT1L1rFXg"
client_secret = "LH_y_XvemI"
encText = urllib.parse.quote("치킨")
urljson = "https://openapi.naver.com/v1/search/blog.json?query=" + encText # json 결과
urlxml = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(urlxml)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()

requestjson = urllib.request.Request(urljson)
requestjson.add_header("X-Naver-Client-Id",client_id)
requestjson.add_header("X-Naver-Client-Secret",client_secret)
responsejson = urllib.request.urlopen(requestjson)
rescodejson = responsejson.getcode()

if(rescode==200):
    response_body = response.read()
    # print(response_body.decode('utf-8'))
    xmlsoup = BeautifulSoup(response_body,'html.parser')
    # print(xmlsoup)
    items = xmlsoup.select("item")
        
    for idx, item in enumerate(items):
        # print("[",idx,"]")
        # print("제목 : ",item.title.text)
        # print()
        # print("내용 : ",item.description.getText())
        # print()
        # print()
        pass
else:
    print("Error Code:" + rescode)
    
    
if(rescodejson==200):
    response_bodyjson = rescodejson.read()
    jsonsoup = BeautifulSoup(response_bodyjson,'html.parser')
    itemsjson = jsonsoup.select("item")
    for idx, item in enumerate(itemsjson):
        print("[",idx,"]")
        print("제목 : ",item.title.text)
        print()
        print("내용 : ",item.description.getText())
        print()
        print()
else:
    print("Error Code:" + rescode)