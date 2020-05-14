import pandas as pd
"""
主要功能：提取数据的经纬度并合并，用于地图显示。
"""
data = pd.read_csv('../Data_pre_deal/处理后.csv')
col = data.columns
for name in col:
    if name == 'lng' or name == 'lat':
        continue
    else:
        del data[name]
lng_lat = []

for i in range(len(data['lng'])):
    lng_lat.append(str(data['lat'][i])+','+str(data['lng'][i]))
data['经纬度'] = lng_lat
# cur = data['经纬度'].unique()
# cur = pd.DataFrame(cur)
data.to_csv('经纬度批量.csv'.format(),sep=',')
# data.to_csv('经纬度.csv'.format(), sep=',', index=True)