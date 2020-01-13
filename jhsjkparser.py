
from bs4 import BeautifulSoup
import re
import time
import json
import requests
pages = set()


def getLinks(newlink):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15'
    }
    global pages
    urlroot = 'http://jhsjk.people.cn/'
    r = requests.get(newlink, headers=headers)
    html = r.text
    bsobj = BeautifulSoup(html, 'html.parser')
    for link in bsobj.findAll('a', href=re.compile("^(result)|^(keyword)")):
        if 'href' in link.attrs:
            if urlroot+link.attrs['href'] not in pages:
                newpage = link.attrs['href']
                print(urlroot+newpage)
                with open('path3.txt', 'a', encoding='utf-8') as f:
                    f.write(json.dumps(urlroot+newpage, ensure_ascii=False)+'\n')
                pages.add(urlroot+newpage)
                time.sleep(1.5)
                getLinks(urlroot+newpage)
    for link in bsobj.findAll('a', href=re.compile("^(http://jhsjk.people.cn/result)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newpage = link.attrs['href']
                print(newpage)
                with open('path3.txt', 'a', encoding='utf-8') as f:
                    f.write(json.dumps(newpage, ensure_ascii=False) + '\n')
                pages.add(newpage)
                time.sleep(1.7)
                getLinks(newpage)
    for link in bsobj.findAll('a', href=re.compile("^(article)")):
        if 'href' in link.attrs:
            if urlroot+link.attrs['href'] not in pages:
                newpage = link.attrs['href']
                print(urlroot+newpage)
                with open('path3.txt', 'a', encoding='utf-8') as f:
                    f.write(json.dumps(urlroot+newpage, ensure_ascii=False)+'\n')
                pages.add(urlroot+newpage)
                time.sleep(1.5)
                getLinks(urlroot+newpage)


getLinks("http://jhsjk.people.cn/")