import requests
from bs4 import BeautifulSoup

url = 'http://localhost/CRAWL/crawl.html'

response = requests.get(url)

if response.status_code == 200:
    html = response.text # <html><head></head><body><table></table></body></html>
    # print(html)
    soup = BeautifulSoup(html, 'html.parser') # html을 끌어땡겨
    findall = soup.find_all("td"); #
    selectone = soup.select_one("table > tr > td")
    selects = soup.select("table > tr > td")
    
    # print(soup)
    # print(findall)
    # print(selectone.text)
    # print(selectone.get_text())

    for i, select in enumerate(selects):
        if i > 1:
            print(select.get_text())
            # print(select.text)

else : 
    print(response.status_code)
    