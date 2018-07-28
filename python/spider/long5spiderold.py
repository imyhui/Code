# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import lxml
import time
import settings
from email.mime.text import MIMEText
import smtplib

def getUrlInfo(url):
    try:
        html = requests.get(url)
    except:
        return None
    soup = BeautifulSoup(html.text, 'lxml')
    before = soup.find("div", {"class":"book_box"});
    title = {}
    title['name'] = before.dt.get_text()
    title['herf'] = url+before.find('a').get('href')[9:]
    data = []

    for dd in before.find_all('span'):
        if(dd.get('style') != None):
            for string in dd.strings:
                data.append(string)
    title['time'] = data[0][-19:]
    title['chapte'] = data[2]
    return title

def getContent(url):
    try:
            html = requests.get(url)
    except:
        with open("log.log","a") as file:
            file.write("Http error on " + time.ctime())
        time.sleep(60)
        return None
    soup = BeautifulSoup(html.text, 'lxml')
    content = soup.find("div", {"id":"chaptercontent"}).get_text()
    return content

def getTimeStamp(timeStr):
    timeArray = time.strptime(timeStr, "%Y-%m-%d %H:%M:%S")
    timeStamp = int(time.mktime(timeArray))
    return timeStamp

def isUpdate(updateTime,lastUpdateTime):
    if(updateTime!=lastUpdateTime and getTimeStamp(updateTime)> getTimeStamp(lastUpdateTime)):
        return True
    return False

def sendMail(to_list,sub,content):
    '''
    to_list:发给谁
    sub:主题
    content:内容
    send_mail("aaa@126.com","sub","content")
    '''
    me=settings.mail_user+"<"+settings.mail_user+"@"+settings.mail_postfix+">"
    # msg = MIMEText(content)
    msg = MIMEText(content,'plain','utf-8')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        s = smtplib.SMTP()
        s.connect(settings.mail_host)
        s.login(settings.mail_user,settings.mail_pass)
        s.sendmail(me, to_list, msg.as_string())
        s.close()
        return True
    except Exception as e:
        print(str(e))
        return False

def sendLog(title,data):
    try:
        sub = title['chapte']+'updated_at'+title['time']
        sendMail(settings.mailto_list,sub,data)
    except:
        with open("log.log","a") as file:
            file.write("Send email error on " + time.ctime() + "\n")
        print("Error on",time.ctime())
        return
    print("Success",time.ctime())






def main():
    lastUpdateTime = '2018-07-20 15:17:58'
    # 初始url
    baseUrl = 'http://m.yunxs.com/'
    url = baseUrl + 'longzu5/'
    title = getUrlInfo(url)
    
    content = getContent(title['herf'])
    content += getContent(title['herf'][:-5]+'_2.html')

    
    if(title!=None):
        updateTime = title['time']
    if(isUpdate(updateTime,lastUpdateTime)):
        sendLog(title,content)
        lastUpdateTime = updateTime

if __name__ == '__main__':
    while True:
        main()
        time.sleep(settings.INTERVALS)
