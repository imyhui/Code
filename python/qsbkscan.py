import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
from email.mime.text import MIMEText
from email.header import Header

url = 'https://www.qiushibaike.com/hot/page/%s/'%str(1)
try:
    html = requests.get(url)
except:
    print("error")
soup = BeautifulSoup(html.text, 'lxml')
data_list = []
for cont in soup.find_all("div", {"class":"content"}):
    raw_data = cont.get_text()
    data = raw_data.replace("\n","")
    data_list.append(data)
'''
for data in data_list:
    print(data)
'''
#print(data_list)
email_text  = ''
for i in data_list:
    email_text += (i + "\n\n")
#############
#要发给谁，这里发给2个人
mailto_list=["1359158019@qq.com"]
#####################
#设置服务器，用户名、口令以及邮箱的后缀
mail_host="smtp.126.com"
mail_user="andyhui686666"
mail_pass="12345asd"
mail_postfix="126.com"
######################
def send_mail(to_list,sub,content):
    '''
    to_list:发给谁
    sub:主题
    content:内容
    send_mail("aaa@126.com","sub","content")
    '''
    me=mail_user+"<"+mail_user+"@"+mail_postfix+">"
    msg = MIMEText(content)
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)
        s.login(mail_user,mail_pass)
        s.sendmail(me, to_list, msg.as_string())
        s.close()
        return True
    except Exception as e:
        print(str(e))
        return False

if send_mail(mailto_list,"笑话",email_text):
    print("发送成功")
else:
    print("发送失败")