import os
import pandas as pd
def readname():
    filePath = 'E:\\2016\\'
    name = os.listdir(filePath)
    return name

if __name__ == "__main__":
    name = readname()
    f1 = pd.read_csv('E:\\2016\\'+ name[0])
    # f2 = pd.read_csv('E:\\洛杉矶Hive下的event_data\\'+ name[1])
    # f = [f1,f2]
    # f_final = pd.concat(f)
    for file in name:
        print(file)
        if file == '2016-1-上半月.csv':
            continue
        f2 = pd.read_csv('E:\\2016\\' + file)
        f = [f1,f2]
        f1 = pd.concat(f)
    f1.to_csv("2016.csv".format(),sep=',', index=False)

