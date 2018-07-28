# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import lxml
import time
import settings
from email.mime.text import MIMEText
import smtplib
global last_chapter
last_chapter = settings.last_chapter

def getUrlInfo(url):
    try:
        html = requests.get(url)
    except:
        return None
    soup = BeautifulSoup(html.text, 'lxml')
    before = soup.find("div", {"class":"book_last"});
    title = {}
    hrefs = before.find_all('a')
    for href in hrefs:
        title[href.get('href')[9:-5]] = href.get_text()
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
        # simple smtp port 25
        # s = smtplib.SMTP()
        # s.connect(settings.mail_host)

        # ssl smtp port 465
        s = smtplib.SMTP_SSL(settings.mail_host,settings.ssl_port)
        s.login(settings.mail_user,settings.mail_pass)
        s.ehlo()

        s.sendmail(me, to_list, msg.as_string())
        s.close()
        return True
    except Exception as e:
        print(str(e))
        return False

def sendLog(title,data):
    try:
        sub = title + time.ctime()
        sendMail(settings.mailto_list,sub,data)
    except:
        with open("log.log","a") as file:
            file.write("Send email error on " + time.ctime() + "\n")
        print("Error on",time.ctime())
        return
    print("Success",time.ctime())



def main():
    global last_chapter
    # 初始url
    baseUrl = 'http://m.yunxs.com/'
    url = baseUrl + 'longzu5/'
    title = getUrlInfo(url)
    maxchapter = int(max(title,key=lambda x:int(x)))

    if(maxchapter>last_chapter):
        title = sorted(title.items())
        for curl,name in title:
            if(int(curl) > last_chapter):
                print(1)
                newurl = url+curl
                content = getContent(newurl+'.html')
                content += getContent(newurl+'_2.html')
                sendLog(name,content)
                last_chapter = int(curl)
    print(last_chapter)
                
if __name__ == '__main__':
    while True:
        main()
        time.sleep(settings.INTERVALS)
