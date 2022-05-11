import csv
import os
import time
import datetime

files = [
"LC2211380007C",
"LC21C13900055",
"LC221099000KW",
"LC21C0890001N",
"LC21B069000R5",
"LC21B22900063",
"FX216100001HM",
"LC21B0890000J",
"LC21B0390007Y",
"LC21B21900016"]

"""
"LC21C219000CE",
"LC20925000018",
"LC21B0390007Y",
"LC21608800084",
"LC2142390000M",
"LC20928000007",
"LC21C0890001N",
"LC21B0390006B",
"LC2192090009C",
"LC2221990000F",
"LC21B1590004Q",
"LC21B11900009",
"FX222170002PP",
"LC21B249000BA",
"FX222170002Q6",
"LC22111900056",
"LC21B2590000L",
"LC22110800011",
"FX222170002R4",
"FX222170002RL",
"LC21A06900061",
"LC21C0890001N",
"LC21B2990001Q",
"LC21C189000CJ",
"LC21C189000AY",
"FX222170002VJ",
"FX222170002Q2",
"FX222170002V8",
"FX222170002Q7",
"FX222170002RN",
"LC21B0390007Y",
"LC21C2190000D",
"LC21C129000RW",
"LC221119000JV",
"LC21B0890000J",
"LC21B159000GY",
"LC21B09900094",
"LC21907900012"]
"""


#path='/home/maomao/LOG-analysis/Error_logs/Logs/'
path='/home/maomao/LOG-analysis/0331/Logs/'

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
            #print("filename:", filename)
            print("files:", files[k])