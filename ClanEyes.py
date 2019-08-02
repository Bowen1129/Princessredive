# -*- coding: utf-8 -*-
import re
import numpy as np
import pandas as pd
from itertools import islice
#读取文件
name=[]
damage=[]
boss=[]
with open('原始数据.txt',encoding= 'utf-8-sig',) as origin_file:
    for line in origin_file.readlines():
        # if re.match('.*が$)', line):
        #     line=line.strip()
        #     line2=line.split('\n')
        #     print(line2)
        # else if re.match('.*ダメージ*.', line):
        #     b=line
#正则
        # if re.match('(.*が$)', line) or re.match('.*ダメージ*.', line) or re.match('.*に$', line):
        if re.match('.*が$', line):
            line=line.strip()
            line_list=line.split('\n')
            name.append(line_list)
            # print(type(line))
        if re.match('.*ダメージ*.', line):
            line = line.strip()
            line_list = line.split('\n')
            damage.append(line_list)
            # print(damage)
        if re.match('.*に$', line):
            line = line.strip()
            line_list = line.split('\n')
            boss.append(line_list)
            # print(type(line))
data={"name":name, "damage":damage, "boss":boss}
data_df=pd.DataFrame(data)
print(data_df)
# a.append(name)
# a.append(damage)
# a.append(boss)
#切片
    # while True:
    #     line2=list(islice(a,3))
    #     if not a:
    #         break
    #     b.append(line2)
    #     print(b)
# data_df=pd.DataFrame(a)
# data_df=data_df.replace('\n','')
# print(data_df)
# data_df.to_csv('washup.csv',encoding='utf-8-sig')