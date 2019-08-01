# -*- coding: utf-8 -*-
import re
import pandas as pd

#读取文件
with open('D:\\shit\\原始数据.txt',encoding= 'utf-8') as origin_file:
    for line in origin_file.readlines():
        line=line.strip()
        # print(line)
result=re.findall( '$ダメージ|$が',line)
print(result)