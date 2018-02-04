#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
filename=sys.argv[1]
print filename
if len(filename)<8:
	print 'filename at least 8 chars'
	sys.exit(1)


def insertSectnum(text):
	'text是immutable的，所以需要返回'
	match='\n\n'
	titleEndAt=text.index(match)+len(match)
	leftText=text[:titleEndAt]
	rightText=text[titleEndAt:]
	text=leftText+"\n\n"+'.. sectnum::'+"\n\n"+rightText
	return text

f = open(filename,'r+')
text=f.read()
text=insertSectnum(text)
f.truncate(0) #先清空，否则在后面追加
f.seek(0)#跳到开始位置
f.write(text)
f.close()

#
#for i in *.txt; do
#	./addsecnum.py $i
#done