#!/usr/bin/env python
# coding=utf-8

'''
fp=open("./file/abc.txt","w+")
fp.write("Hello,World,itcast!")
fp.flush()
fp.close()
'''

'''
fp=open("./file/abc.txt","r")
mybuf=fp.readlines()
print mybuf
fp.close()
'''

fp1=open("./file/abc.txt","r")
fp2=open("./file/abc_new.txt","w")

while True:
    buf=fp1.readline()
    if buf=='':
        break
    fp2.write(buf)

fp1.close()
fp2.close()

