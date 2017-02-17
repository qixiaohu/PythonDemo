#!/usr/bin/env python
# coding=utf-8

class Student:
    #静态成员变量
    age=18

    #类的对象的方法，相当于C++中普通成员函数
    def __init__(self,name):
        self.name=name

    def showMe(self):
        print self.name

    #类的方法,相当于C++中的静态成员函数
    #类方法的装饰器
    @classmethod     
    def getAge(cls):
        return cls.age   

if __name__=="__main__":
    s1=Student("zhang3")
    s1.showMe()

    #类名.FuncName[通过类名直接调用类的方法]
    print Student.getAge()
