import pandas as pd
"""
主要功能：主要提取经纬度的唯一值。
"""
data = pd.read_csv('../Data_pre_deal/2016_经纬度+时间.csv')
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
cur = data['经纬度'].unique()
cur = pd.DataFrame(cur)

# cur.to_csv('b.csv'.format(),sep=',')
cur.to_csv('2016经纬度唯一值.csv'.format(), sep=',', index=True)