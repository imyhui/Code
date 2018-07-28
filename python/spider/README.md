# 小说更新推送爬虫

> 基于python2.7的爬虫，作用为定时爬取小说网站文章列表，判断是否更新，若更新则以邮件形式发送到邮箱,由于是定向爬虫，仅限对指定网站的指定小说。


## 使用
- 安装python2.7
- 安装以下依赖
	- bs4 
	- lxml
	- smtplib

- 设置参数
	- 编辑settings.py
	- 将xxxx内容补全

- 本地测试
	> python2.7 long5spidernew.py
	
- 服务器长期运行
	> nohup python -u long5spidernew.py > test.log 2>&1 &


## 实现思路及分析
参照[这里](http://andyhui.xin/blog/long5-spider)