#!/usr/bin/env python
# coding=utf-8

#标准输入
print "Please input your name:"
name=raw_input()
print "Hello %s,Welcome to coding world!" %(name)

#python默认的标准输入为字符串格式
print type(name)

#强制类型装换
num=int(name)
print type(num)

