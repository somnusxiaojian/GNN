import os
import pandas as pd
import numpy as np
import json


"""
提取主要的数据，并将时间分为年-月-日-时-分。
"""
data = pd.read_csv('../Contact_Data/2016.csv')
col = data.columns
location = data['event_data.location']
time = data['event_data.start_time']

def DateSplit(df, col):
    """
    split the object of '2010-01-02' into year(2010), month(1) and day(2).
    :param df:  to operate data （type：DataFrame）
    :param col: column label of date object （type：str）
    :return: converted date （type： DataFrame）
    """
    year, month, day, hour, minute = [], [], [], [], []
    data = df.loc[:, col].values
    #df = df.drop([col], axis=1)

    for i in range(data.shape[0]):
        year.append(int(data[i][:4]))
        month.append(int(data[i][5:7]))
        day.append(int(data[i][8:10]))
        hour.append(int(data[i][11:13]))
        minute.append(int(data[i][14:16]))
        #second.append(int(data[i][17:]))
    date = pd.DataFrame({'year': year, 'month': month, 'day': day,'hour':hour,'minute':minute})
    result = pd.concat([date, df], axis=1)
    return result

#data= DateSplit(df=data,col='event_data.start_time')
lng = [] # 经度
lat = [] # 纬度
for value in location:
    value = eval(value)
    lng.append(value['lng'])
    lat.append(value['lat'])
data['lng'] = lng
data['lat'] = lat
#data['description'] = data['event_data.description']
#data['admin_city'] = data['event_data.admin_city']
#data['comment_external_content'] = data['event_data.comment_external_content']
data['time'] = data['event_data.start_time']
for name in col:
    del data[name]
# for i in range(len(data)):
#     if data.iloc[i]['lat'] == 0:
#         data.drop([i])
#         print(i)
data.to_csv('2016_经纬度+时间.csv'.format(), sep=',', index=True)

