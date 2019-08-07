# -*- coding: utf-8 -*-
import re
import pandas as pd
import time
import os
#建立路径文件
path="D:\shit\天眼系统"
    # if not os.path.exists(path):
    #     os.mkdir(path)
#时间戳
df_time=time.strftime("%Y-%m-%d", time.localtime())
file_name=path+'\%s.xlsx'%df_time
writer=pd.ExcelWriter(file_name)
#读取文件
name=[]
damage=[]
boss=[]
with open('原始数据.txt',encoding= 'utf-8-sig',) as origin_file:
    for line in origin_file.readlines():
#正则
        # if re.match('(.*が$)', line) or re.match('.*ダメージ*.', line) or re.match('.*に$', line):
        if re.match('.*が$', line):
            line=line.strip()
            line=line.replace("が",'')
            line_list=line.split('\n')
            name.append(*line_list)
        #     print(line)
        if re.match('.*ダメージ*.', line):
            line = line.strip()
            result=re.compile('([^ダ]+)([ダ*.])')
            num=result.search(line)
            num=num.group(1)
            line_list = num.split('\n')
            damage.append(*line_list)
            # print(damage)
        if re.match('.*に$', line):
            line = line.strip()
            line = line.replace("に", '')
            line_list = line.split('\n')
            boss.append(*line_list)
            # print(type(line))
#输出表
data={"name":name, "damage":damage, "boss":boss,"count":""}
data_df=pd.DataFrame(data)
data_df=pd.pivot_table(data_df,index=["name","damage", "boss"], values="count", aggfunc='count')
grouped=data_df.groupby('name')['count'].sum()
data_df.to_excel(writer, sheet_name='详表')
grouped.to_excel(writer, sheet_name='刀数')
writer.save()
# print(grouped)
# for name,group in  data_df.groupby(['name', 'damage', 'boss']):
#      data_df=data_df.groupby('count').sum()
# print(data_df)
# print(data_df.describe())
# data_df.to_csv(df_time+'处理完成.csv',encoding='utf-8-sig')