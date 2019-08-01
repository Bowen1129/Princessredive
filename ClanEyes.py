# -*- coding: utf-8 -*-
import re
import pandas as pd

#读取文件
with open('D:\\shit\\原始数据.txt',encoding= 'utf-8') as origin_file:
    for line in origin_file.readlines():
        line=line.strip()
        # print(line)
#匹配信息
        if re.match('(.*が$)', line) or re.match('.*ダメージ$', line ) or re.match('.*に$', line ):
            print(line.strip())