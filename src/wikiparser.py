
from bs4 import BeautifulSoup
import re
import time
import json
import requests
from jieba import analyse


pages = set()
count = 0


def getLinks(newlink):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15'
    }
    global pages
    global count
    urlroot = 'http://jhsjk.people.cn/'
    r = requests.get(newlink, headers=headers)
    html = r.text
    bsobj = BeautifulSoup(html, 'html.parser')
    result = re.match('^http://jhsjk.people.cn/article/', newlink)
    print("result")
    print(result)
    if result != None:
        filename = str(count)+'.txt'
        count += 1
        content=""
#get databasetitle
        for item in bsobj.find_all(name='title'):
#        print(item.get_text())
            content+=item.get_text().strip()+"\n"
#get title
        for item in bsobj.find_all(name=re.compile('^(h\d)')):
#        print(item.get_text())
            content+=item.get_text().strip()+"\n"
#get launch time
        result = re.search('<div.*?&nbsp;&nbsp;(.*?)</div>', html, re.S)
#    print(result.group(1))
        content+=result.group(1).strip()+"\n"
#get text
        for item in bsobj.find_all(name='p'):
            content+=item.get_text()
#        print("printing......"+item.get_text())
#关键词信息写入文件
        f = open(filename, "w")
        tfidf = analyse.extract_tags
        keywords = tfidf(content)
        g = open("keyword.txt", "a")
        g.write(filename+"\n")
        f.write("关键词：\n")
        for keyword in keywords:
            print(keyword)
            g.write(keyword + " ")
            f.write(keyword + " ")
        g.write("\n")
        f.write("\n\n")
        f.write(content)
        g.close()
        f.close()
#获取网页中新的链接的信息并继续爬
    for link in bsobj.findAll('a', href=re.compile("^(result)|^(keyword)")):
        if 'href' in link.attrs:
            if urlroot+link.attrs['href'] not in pages:
                newpage = link.attrs['href']
                print(urlroot+newpage)
                with open('path4.txt', 'a', encoding='utf-8') as f:
                    f.write(json.dumps(urlroot+newpage, ensure_ascii=False)+'\n')
                pages.add(urlroot+newpage)
                time.sleep(1.5)
                getLinks(urlroot+newpage)
    for link in bsobj.findAll('a', href=re.compile("^(http://jhsjk.people.cn/result)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newpage = link.attrs['href']
                print(newpage)
                with open('path4.txt', 'a', encoding='utf-8') as f:
                    f.write(json.dumps(newpage, ensure_ascii=False) + '\n')
                pages.add(newpage)
                time.sleep(1.7)
                getLinks(newpage)
    for link in bsobj.findAll('a', href=re.compile("^(article)")):
        if 'href' in link.attrs:
            if urlroot+link.attrs['href'] not in pages:
                newpage = link.attrs['href']
                print(urlroot+newpage)
                with open('path4.txt', 'a', encoding='utf-8') as f:
                    f.write(json.dumps(urlroot+newpage, ensure_ascii=False)+'\n')
                pages.add(urlroot+newpage)
                time.sleep(1.5)
                getLinks(urlroot+newpage)


url = 'http://jhsjk.people.cn/'
url1 = 'http://jhsjk.people.cn/article/28855099'
url2 = 'http://jhsjk.people.cn/article/30284771'
url3 = 'http://jhsjk.people.cn/article/30254137'
url4 = 'http://jhsjk.people.cn/article/30269698'
url5 = 'http://jhsjk.people.cn/article'
getLinks(url)