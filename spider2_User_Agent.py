#!/usr/bin/env python
# coding=utf-8

import urllib2

#请求的URL
url="http://www.baidu.com"

#组织User-Agent
User_agent="Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0"
header={"User-Agent":User_agent}

#访问URL
request=urllib2.Request(url,headers=header)

response=urllib2.urlopen(request)

html_text=response.read()

print html_text
