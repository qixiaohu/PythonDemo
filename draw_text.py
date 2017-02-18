#!/usr/bin/env python
# coding=utf-8

import Image,ImageFont,ImageDraw

myPath="/home/itcast/python"
fontPath="/home/itcast/python"

inputFile="0735-niutuku.com-135.jpg"
outputFile="output.jpg"

#打开图片
im=Image.open(myPath+inputFile)
draw=ImageDraw.Draw(im)

#根据图片大小确定字体大小
fontsize=min(im.size)/4

#加文字
myfont=ImageFont.truetype(fontPath+"SIMYOU.TTF",fontsize)

#通过画家在 图片上画出 文字
draw.text((im.size[0]-fontsize,0),"9",font=myfont,fill=(256,0,0))
#jpeg  是文件的存储格式，并不是文件的后缀名
im.save(myPath,outputFile,"jpeg")
