#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
filename=sys.argv[1]
print filename
if len(filename)<8:
	print 'filename at least 8 chars'
	sys.exit(1)

f = open(filename,'r+')
text='.. sectnum::' + "\n\n\n" + f.read()
f.truncate(0) #先清空，否则在后面追加
f.seek(0)#跳到开始位置
f.write(text)
f.close()

#
#for i in *.txt; do
#	./addsecnum.py $i
#done