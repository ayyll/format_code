#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-29 17:42:23
# @Author  : ayyll (upyh@foxmail.com)
# @Link    : http://ayyll.com
# @Version : V-1.0.0

import os
import sys

#获取当前目录下的文件
file_arr = os.listdir(os.getcwd())
for i in range(len(file_arr)):
    if file_arr[i].endswith('.c') or file_arr[i].endswith('.h'):
        print 'now we are repairing the ' + file_arr[i] + '...'
        file_obj = open(file_arr[i],'r')
        ans = ''
        try:
            for eachline in file_obj:
                
                line_lstrip = eachline.lstrip()
                line_strip = eachline.strip()
                line_rstrip = eachline.rstrip()

                if eachline.startswith('{') == False and cmp(line_strip,'{') == 0:
                    continue;

                if line_lstrip.startswith('if') and line_rstrip.endswith('{') == False:
                    ans += (eachline[0:len(eachline) - 1] + ' {\n')
                elif line_lstrip.startswith('else') and line_rstrip.endswith('{') == False:
                    ans = ans[0:len(ans) - 1]
                    ans += ' else {\n'
                elif line_lstrip.startswith('for') and line_rstrip.endswith('{') == False:
                    ans += (eachline[0:len(eachline) - 1] + ' {\n')
                else:
                    ans += eachline

            #print ans
        finally:
            file_obj.close()

        #写文件,覆盖的方式
        file_obj = open(file_arr[i],'w')

        try:
            file_obj.write(ans)
        finally:
            file_obj.close()

print 'Formatting Successful!'
os.system("pause")