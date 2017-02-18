#!/usr/bin/env python
# coding=utf-8

tieba_url = "http://tieba.baidu.com/f?kw=lol&ie=utf-8&pn="
#pn = 0   第一页
#pn = 1   第二页
#pn = 100 第三页

#pn = 50*(page-1)

import urllib2

def write_file(filename,text):
    print "正在存储"+filename
    fp=open(filename,"w")
    fp.write(text)
    fp.close()

def load_page(url):
    
    #请求的URL
    url="http://www.baidu.com"

    #组织User-Agent
    User_agent="Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0"
    header={"User-Agent":User_agent}

    #访问URL
    request=urllib2.Request(url,headers=header)

    response=urllib2.urlopen(request)

    html_text=response.read()
    return html_text


def tieba_spider(begin_page,end_page):
    for page in range(begin_page,end_page+1):
        print "开始存储第" + str(page) + "页"
        pn=50*(page-1)
        temp_url=tieba_url+str(pn)
         
        html_text=load_page(temp_url)

        filename=str(page)+".html"
        write_file(filename,html_text)

if __name__=="__main__":
    begin_page=int(raw_input("请输入爬取开始页面："))
    end_page=int(raw_input("请输入爬取结束页面："))

    print begin_page
    print end_page

    #开始爬取
    tieba_spider(begin_page,end_page)

    #爬取结束
    print "爬取完毕！"


