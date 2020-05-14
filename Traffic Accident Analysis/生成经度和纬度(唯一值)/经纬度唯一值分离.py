import pandas as pd
"""
将经纬度分离，这个经纬度都是唯一的。不存在重复的。
"""

data = pd.read_csv('../提取经纬度的唯一值/2016经纬度唯一值.csv')
col = ['index','cur']
data.columns = col
data['cur'] = data['cur'].str.split(',')
data['lat'] = data['cur'].map(lambda x:x[0])
data['lon'] = data['cur'].map(lambda x:x[1])
data.to_csv('2016_经纬度.csv'.format(), sep=',',index=False)