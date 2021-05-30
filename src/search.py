import re


def searchintext(searchText):
    f=open('fenci.txt','r')
    for line in f.readlines():
        result = line.startswith(searchText)
        if result==True:
            print(line)
            ret=line.split()
            return ret

t=searchintext('党中央')
print(searchintext('党中央'))
l=len(searchintext('党中央'))
for i in range(1,l):
    print(t[i])