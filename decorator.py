#!/usr/bin/env python
# coding=utf-8

#装饰器函数
def doc_func(func):
    #包裹函数[闭包，额外需要添加的功能全部在此函数中添加]
    def warpfunc():
        #做一些额外的功能
        print "%s called" %(func.__name__)
        #生调一下被装饰的函数
        func()

    #返回内部函数
    return warpfunc

#在被装饰的函数前面显示调用装饰函数
@doc_func
def foo():
    print "Hello"

@doc_func
def bar():
    print"World"

#程序的入口
if __name__=="__main__":
    foo()
    bar()
