#!/usr/bin/python3
# -*- coding: utf-8 -*-

import csv

# 1. 
f = open('log.csv', 'w', encoding='utf-8', newline="")

csv_writer = csv.writer(f)

# 3. create table head
#csv_writer.writerow(["name","age","male"])

# 4. 写入csv文件内容
#csv_writer.writerow(["l",'18','male'])
#csv_writer.writerow(["c",'20','fe'])
#csv_writer.writerow(["w",'22','fe'])

# 5. 关闭文件


import os
#import xlsxwriter as xw
import subprocess
import time
import datetime

#cmd='./test-run1.sh '+str(empu_num[l]) + ' ' + str(batch[k1])
#grep "timestamp" converted_Tencent_FX21B050001PD_2022-01-17-09-55_RegRawData_1.json | awk '{print $2}'
filename='converted_Tencent_FX21B050001PD_2022-01-17-09-55_RegRawData_1.json';
get_data_cmd='grep ' + 'timestamp '+ filename + '| awk \'{print $2}\''
print("get_data_cmd: ", get_data_cmd)
#get_data_cmd='cat ' + filename + '| grep "\<latency\>" | awk \'{sum+=$7} END {print sum/NR}\''
latency = subprocess.check_output(get_data_cmd, shell=True)
#latency=float(latency.strip())
print("latency : ", latency)
data=str(latency, 'utf-8')

print ("latency[0]: ", latency[1:20])
print ("data[0]: ", data[1:20])
time=data[1:20]
#2022-01-08T09:25:57

get_data_cmd='grep ' + time + ' onekeylog/log/ -rn' + '| grep idl'
print("get_data_cmd: ", get_data_cmd)
#grep 2022-01-08T09:25:57  -rn | grep idl
latency = subprocess.check_output(get_data_cmd, shell=True)
#latency=float(latency.strip())
data=str(latency, 'utf-8')
print("idl: ", data)
#data=str(latency, 'utf-8')
start=data.find('|')
Diagnose_info=data[start:]
print("Diagnose_info:", Diagnose_info)

data_slice=data.split(' ')
print("data_slice:", data_slice)
print("data_slice[3]:", data_slice[3])
print("data_slice[4]:", data_slice[4])
meachine=data_slice[3]
InspurDiagnose=data_slice[4]

csv_writer.writerow([time,meachine,InspurDiagnose, Diagnose_info])

f.close()
