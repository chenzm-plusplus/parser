from bs4 import BeautifulSoup
import requests
import re
import codecs
import jieba
import jieba.posseg
import json
from collections import Counter
from  jieba import analyse

url = 'http://jhsjk.people.cn/article/28855099'
url2 = 'http://jhsjk.people.cn/article/30284771'
url3 = 'http://jhsjk.people.cn/article/30254137'

headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15'
    }
r = requests.get(url2, headers=headers)

soup = BeautifulSoup(r.text, "html.parser")

print(soup.prettify())


def readfile(filename):
    content = ""
    try:
        fo = jieba.open(filename, 'r', 'utf-8')
        for line in fo.readlines():
            content+=line.strip()
    except IOError as e:
        print("fail")
        return ""
    else:
        fo.close()
        return content


def writefile( toFile, content):
    try:
        fo = codecs.open(toFile, 'a', "utf-8")
        print("文件名：", toFile)
        if isinstance(type(content), type([])):
            fo.writelines(content)
            print("writing")
        else:
            print("writing")
            fo.write(content)
    except IOError:
        print("fail")
    else:
        print("success")
        fo.close()


content = ""
print(soup.title.string)
print(soup.h1.string)
for item in soup.find_all(name='title'):
    print(item.get_text())
    content += item.get_text()+'\n'
for item in soup.find_all(name=re.compile('^(h\d)')):
    print(item.get_text())
    content += item.get_text()+'\n'
for item in soup.find_all(name='p'):
    content += item.get_text()+'\n'
seg_list = jieba.cut_for_search(content)
c = Counter(content).most_common(10)
print(type(c))
print(c)
tfidf = analyse.extract_tags
keywords = tfidf(content)
#分词结果和关键词写入文件
f=open("temp.txt", "w")
g=open("keyword.txt", "a")
g.write("filename\nkeyword:")
f.write("关键词:")
for keyword in keywords:
    print(keyword)
    f.write(keyword+' ')
    g.write(keyword+" ")
f.write('\n')
g.write('\n')
f.write(" ".join(seg_list))
f.close()
g.close()

wordlist=[]
wordcount={}