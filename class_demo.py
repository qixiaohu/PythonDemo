#!/usr/bin/env python
# coding=utf-8

class Student:
    '''学生类'''

    #在C++中的私有成员，在Python中用类的成员表示【类.成员】
    school='itheima'

    def __init__(self,name,age):
        '''构造函数'''
        #C++中的普通成员，在Python中叫做对象的成员【self.成员】
        self.name=name
        #Python中的静态成员在成员名称的前面加前缀"__"
        self.__age=age
        print "__init__"
    
    def showMe(self):
        '''普通函数'''
        print "in show().."
        print self.name
        print self.__age

    def __del__(self):
        '''析构函数'''
        print"__delete__"

#程序入口
if __name__=="__main__":
    s1=Student("zhang3",18)
    s1.showMe()
    print Student.school
    print ("*")*30
    #在类的外部访问类的私有成员，不会有语法错误，但是修改也不会生效
    s1.__age=100
    s1.showMe()
    
    print ("*")*30
    #在类的外部修改类的成员【相当于C++的私有成员】
    Student.school="itcaast"
    print Student.school

