import re
import jieba
from jieba import analyse

count=0
d={'':0}
p={'':''}

def fenci():
    global d
    global count
    global p
    s={}
    filename = str(count)+'.txt'
    count+=1
    print(filename)
    f=open(filename,'r')
    content=f.read()
    seg_list=jieba.cut_for_search(content)
    for sword in seg_list:
        word=sword.strip()
        if word.strip() in s:
            s[word]+=1
        else:
            s[word]=1
    for word in s:
        if word in p:
            p[word]+=" "+filename
        else:
            p[word]=filename


for i in range(4706):
    fenci()

g=open("fenci.txt", 'w')
print(d)
for word in p:
    print(word," ",p[word])
    g.write(word+" "+p[word]+'\n')
g.close()