#_*_ coding:utf-8 _*_
import re
import requests
import os


def downloadPic(counts,keyword):
    urls = [ 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word='+keyword+'&pn='+str(x*60)+'&gsm=3c&ct=&ic=0&lm=-1&width=0&height=0' for x in range(0,counts//60)]
    #print(urls)

    i = 0
    print('找到关键词:'+keyword+'的图片，现在开始下载图片……')
    for each in urls:
        pic_html = requests.get(each, timeout = 10).text
        pic_url = re.findall('"objURL":"(.*?)",', pic_html, re.S)
        for pi in pic_url:
            print('正在下载第'+str(i+1)+'张图片，图片地址：'+str(pi))
            try:
                pic = requests.get(pi, timeout = 10)
            except requests.exceptions.ConnectionError:
                print('【错误】当前图片无法下载')
                continue
            string = keyword+'\\'+keyword+'_'+str(i)+'.jpg'
            fp = open(string,'wb')
            fp.write(pic.content)
            fp.close()
            i += 1

if __name__ == '__main__':
    word = input("Input key word:")
    counts = int(input("Input counts:(min60)"))
    
    #建立对应文件夹
    cur_path = os.path.abspath(os.curdir)
    #获取当前路径
    goal_path = cur_path + '\\' + word
    os.mkdir(goal_path)
    #爬取过程
    downloadPic(counts,word)
