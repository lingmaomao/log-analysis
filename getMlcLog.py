import csv
import os
import time
import datetime

files=[
"LC21B29900015",
"X21A260008A2",
"LC21A21900059",
"FX21B05000227",
"LC21A199000C9",
"LC21A199000DK",
"LC2192790002V",
"LC21820900036",
"LN2172410001F",
"LC2182890000L"
]

path='/home/maomao/LOG-analysis/Error_logs/Logs/'
for k in range(len(files)):
    #print(files[k])
    #filename='/home/maomao/LOG-analysis/Error_logs/Logs/Tencent_LC2192090009A_2022-01-17-09-53/onekeylog/component/component.log'
    #filename='./component.log'
    dirs=os.listdir(path)
    #print("dirs:", dirs)
    for m in range(len(dirs)):
        if (dirs[m].find(files[k])!=-1):
            #print("dir:", dirs[m])
            #print("file:", files[k])
            #print("m:", m)
            #print("k:", k)

            #filename = path+dirs[m]+'/onekeylog/component/component.log'
            filename = path+dirs[m]
            print("filename:", filename)