#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-23 16:27:40
# @Author  : ayyll (upyh@foxmail.com)
# @Link    : http://ayyll.com
# @Version : V-1.0.0

import os
import sys

#获取当前目录下的文件
file_arr = os.listdir(os.getcwd())
for i in range(len(file_arr)):
	if file_arr[i].endswith('.c'):
		print 'now we are repairing the ' + file_arr[i] + '...'
		file_obj = open(file_arr[i],'r')

		try:
			all_the_text = file_obj.read()
		finally:
			file_obj.close()

		ans = all_the_text.replace('\t','    ')

		#写文件,覆盖的方式
		file_obj = open(file_arr[i],'w')

		try:
			file_obj.write(ans)
		finally:
			file_obj.close()

print 'Formatting Successful!'
os.system("pause")