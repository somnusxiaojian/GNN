import pandas as pd
data = pd.read_csv('处理后.csv')

"""需要的时间戳，每半个小时为单位"""
dt_hour=pd.date_range('2016-01-01 00:00','2016-01-02 23:00', freq='30min')
"""需要的时间戳，每一个月为单位"""
dt_month = pd.date_range('2016-01-01 00:00','2016-12-31 23:59',freq='m')
print(dt_month)
"""添加哑变量"""
for i in range(len(dt_need)):
    data['time_'+'%s' %i] = [0] * len(data)


print(data)
