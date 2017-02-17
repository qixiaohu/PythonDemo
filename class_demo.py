#!/usr/bin/env python
# coding=utf-8

class Student:
    '''学生类'''
    def __init__(self,name,age):
        '''构造函数'''
        self.name=name
        self.age=age
        print "__init__"
    
    def showMe(self):
        '''普通函数'''
        print "in show().."
        print self.name
        print self.age

    def __del__(self):
        '''析构函数'''
        print"__delete__"

#程序入口
if __name__=="__main__":
    s1=Student("zhang3",18)
    s1.showMe()
