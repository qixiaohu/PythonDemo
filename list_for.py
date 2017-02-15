#!/usr/bin/env python
# coding=utf-8

fruit=["apple","bnaner","origan",1,3,4]

for item in fruit:
    if type(item)==type(0):
        print item 
        print type(item)
    elif type(item)==type(""):
        print item
