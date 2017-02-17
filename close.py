#!/usr/bin/env python
# coding=utf-8

#外部函数
def outFunc():
    #局部变量
    count=[0]
    
    #内部函数
    def inFunc():
        count[0]=count[0]+1
        return count

    #返回内部函数
    return inFunc

