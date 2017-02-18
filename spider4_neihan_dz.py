#coding=utf-8

import urllib2,re

#第一页 http://www.neihan8.com/article/index.html
#其他页码 http://www.neihan8.com/article/index_[x].html

#匹配规则
#得到段子的url路径  <h3><a href="()"
#得到段子标题的      <h1 class="title">()h1>
#得到段子内容的      a>p>()<div class="ad610">

class Spider:
    '''爬虫类'''
    def __init__(self):
        self.page=1

    def load_page(self,url):
        #模拟狐火浏览器
        user_agent="Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0"
        header={"User-Agent":user_agent}
        request=urllib2.Request(url,headers=header)
        #发送URL请求
        response=urllib2.urlopen(request)
        #得到返回数据
        html_text=response.read()
        return html_text

    def spider_one_page(self):
        '''爬取第page页，同时得到该页面的全部段子的url列表'''
        if(self.page==1):
            url="http://www.neihan8.com/article/index.html"
        else:
            url="http://www.neihan8.com/article/index_"+str(self.page)+".html"
        html_text=self.load_page(url)

        #  print html_text
        #得到全部的 段子的 URL地址
        pattern=re.compile('<h3><a href="(.*?)"', re.S)
        dz_url_list=pattern.findall(html_text)
        print dz_url_list
        return dz_url_list


    def save_title_content_list(self,titles,contents):
        '''将标题和内容写到文件中'''
        print "正在保存 第" +str(self.page) + "页的全部段子"
        for i in range(len(titles)):
            contents[i]=contents[i].replace("\r\n","")\
                                   .replace("<div>","")\
                                   .replace("</div>","")\
                                   .replace("<p>","")\
                                   .replace("</p>","")\
                                   .replace("&ldquo;","")\
                                   .replace("&rdquo;","")\
                                   .replace("&nbsp;","")\
                                   .replace("&hellip;","")
            self.write_one_dz(titles[i],contents[i])


    def write_one_dz(self,title,content):
        fp=open('./myDuanZi.txt',"a")
        fp.write("="*15)
        fp.write("\n")
        fp.write(title)
        fp.write("\n")
        fp.write("="*15)
        fp.write("\n")
        fp.write(content)
        fp.write("\n")
        fp.close()

    
    def spider_dzurl_list(self,url_list):
        '''根据url_list分别请求段子的网页，爬取段子的内容'''

        titles=[]
        contents=[]

        for url in url_list:
            dz_url="http://www.neihan8.com"+url
            html_text=self.load_page(dz_url)

            #得到段子的标题
            pattern=re.compile('<h1 class="title">(.*?)</h1>',re.S)
            title=pattern.findall(html_text)
            titles.append(title[0])

            #得到段子的内容
            pattern=re.compile('</a></p>(.*?)<div class="ad610">',re.S)
            content=pattern.findall(html_text)
            contents.append(content[0])
        #将标题和数据保存到文件中
        self.save_title_content_list(titles,contents)
    
    def doWork(self):
        '''爬虫的主业务方法'''

        while True:
            print "输入回车 爬取下一行"
            print "输入exit退出"
            cmd=raw_input()
            if(cmd=="exit"):
                break
            
            #开始爬取
            dz_url_list=self.spider_one_page()
            self.spider_dzurl_list(dz_url_list)

            #爬取该页面完毕
            print "爬取" +str(self.page)+"页 完毕"
            self.page += 1
            

if __name__=="__main__":
    sp=Spider()

    sp.doWork()
