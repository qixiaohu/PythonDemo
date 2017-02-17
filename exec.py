#!/usr/bin/env python
# coding=utf-8
import string
import random

data=string.letters+string.digits
mystr=[]
mystr1=''

for i in range(4):
    for j in range(4):
        mystr1+=random.choice(data)
    mystr.insert(i,mystr1)
    mystr1=''

print '-'.join(mystr)
