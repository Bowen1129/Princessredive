# -*- coding: utf-8 -*-
import re
import numpy as np
import pandas as pd
from itertools import islice
#读取文件
a=[]
b=[]
with open('原始数据.txt',encoding= 'utf-8',) as origin_file:
    for line in origin_file.readlines():
        if re.match('(.*が$)', line) or re.match('.*ダメージ*.', line) or re.match('.*に$', line):
            a=line
            f1=open("washup.txt","a+",encoding='utf-8')
            f1.write(line)
            f1.close()
    # print(a)
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
#匹配信息
# data_df = pd.DataFrame(data=info, columns=['Name', 'Damage', 'Boss'])
# print(data_df)
    # data_dfname.to_csv('damage.csv')
# print(re.match('(.*が$)', line))
# print(data_df)