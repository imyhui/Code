#ojrankscan.py
import requests
import re
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def fillscoreList(slist, html,num):
    rege = r'<a href=.*?>(0{0,1}'+str(num)+'营.*?)</a><td><a href=.*?>([0-9]{1,2})</a>'
    score = re.findall(rege,html)
    for x in score:
        slist.append(x)

def printscoreList(slist, num):
    tplt = "{0:20}\t\t{1:^3}"
    print(tplt.format("xx营xx号_Nickname_name","     解决题目数",chr(12288)))
    for i in range(num):
        u=slist[i]
        print(tplt.format(u[0],u[1],chr(12288)))
def addtodit(slist,idit):
    for (x,y) in slist:
        if idit.__contains__(x):
            idit[x] += int(y)
        else:
            idit[x] = int(y)
def printallsolve(sdit):
    print("*"*12,"每人总解决题目数","*"*17)
    tplt = "{0:20}\t\t{1:^3}"
    print(tplt.format("xx营xx号_Nickname_name","   解决总题目数",chr(12288)))
    for name,values in sdit.items():
        print(tplt.format(name,values,chr(12288)))

def main():
    num = int(input("请输入营号:"))
    sdit = {}
    for no in range(1166,1169):
        sinfo = []
        url = 'http://oj.acmclub.cn/contestrank.php?cid='+str(no)
        html = getHTMLText(url)
        fillscoreList(sinfo, html, num)
        addtodit(sinfo,sdit)
        print("*"*15,"第%d周%d营成绩"%(int(no-1165),num),"*"*18)
        printscoreList(sinfo, len(sinfo))
    '''
    sinfo = []
    url = 'http://oj.acmclub.cn/contestrank.php?cid=1173'
    html = getHTMLText(url)
    fillscoreList(sinfo, html, num)
    addtodit(sinfo,sdit)
    print("*"*15,"结课测试%d营成绩"%(num),"*"*18)
    printscoreList(sinfo, len(sinfo))
    '''
    printallsolve(sdit)
main()