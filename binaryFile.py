#!/usr/bin/env python
# coding=utf-8

import struct

fp=open("./file/binary.dat",'w')
fp.write(struct.pack("6sid","itcast",100,3.14))

fp.close()

fp=open("./file/binary.dat","r")
(name,id,score)=struct.unpack("6sid",fp.read())
print name
print id
print score
