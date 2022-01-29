#!/usr/bin/python3
# -*- coding: utf-8 -*-

import csv

# 1. 
f = open('log.csv', 'w', encoding='utf-8', newline="")
csv_writer = csv.writer(f)

#logs=["idl.log", "selelist.csv", "maintenance.log"]
logs=["idl.log", "maintenance.log"]

import os
#import xlsxwriter as xw
import subprocess
import time
import datetime

#cmd='./test-run1.sh '+str(empu_num[l]) + ' ' + str(batch[k1])
#grep "timestamp" converted_Tencent_FX21B050001PD_2022-01-17-09-55_RegRawData_1.json | awk '{print $2}'

#1.get timeStamp
filename='/home/maomao/LOG-analysis/converted_Tencent_FX21B050001PD_2022-01-17-09-55_RegRawData_1.json';
get_data_cmd='grep ' + 'timestamp '+ filename + '| awk \'{print $2}\''
print("get_data_cmd: ", get_data_cmd)
latency = subprocess.check_output(get_data_cmd, shell=True)
print("latency: ", latency)
data=str(latency, 'utf-8')

print ("latency[0]: ", latency[1:20])
print ("data[0]: ", data[1:20])
time=data[1:20]
#2022-01-08T09:25:57

#2.extract info use timeStamp
for l in range(len(logs)):
    print("log-type: ", logs[l])
    get_data_cmd='grep ' + time + ' /home/maomao/LOG-analysis/onekeylog/log/ -rn' + '| grep '+ logs[l]
    print("get_data_cmd: ", get_data_cmd)
    #grep 2022-01-08T09:25:57  -rn | grep idl
    latency = subprocess.check_output(get_data_cmd, shell=True)
    data=str(latency, 'utf-8')
    print("data: ", data)
    data.rstrip('\n')
    print("data.rstrip(): ", data)

    #ldl.log
    if l == 0:
        start=data.find('|')
        Diagnose_info=data[start:]
        print("Diagnose_info:", Diagnose_info)

        data_slice=data.split(' ')
        print("data_slice:", data_slice)
        print("data_slice[3]:", data_slice[3])
        print("data_slice[4]:", data_slice[4])
        meachine=data_slice[3]
        InspurDiagnose=data_slice[4]
        csv_writer.writerow([time, logs[l], meachine,InspurDiagnose, Diagnose_info])

    #selelist.csv
    #01/08/2022,09:25:57

    #maintenance.log
    if l == 1:
        line_slice=data.split('\n')
        print("line_slice:", line_slice)
        print("line_slice.len:", len(line_slice))
        print("line_slice[0]:", line_slice[0])
        for m in range(len(line_slice)):
            print("m=", m)
            print("m.len=", len(line_slice[m]))
            if len(line_slice[m])==0:
                continue
            print("line_slice[m]:", line_slice[m])
            start=line_slice[m].find('|')
            if start==-1:
                start=line_slice[m].find('[')
            print("start=", start)
         
            Diagnose_info=line_slice[m][start:]
            print("Diagnose_info:", Diagnose_info)
         
            data_slice=line_slice[m].split(' ')
            print("data_slice:", data_slice)
            print("data_slice[3]:", data_slice[3])
            print("data_slice[4]:", data_slice[4])
            meachine=data_slice[3]
            InspurDiagnose=data_slice[4]
            csv_writer.writerow([time,logs[l], meachine,InspurDiagnose, Diagnose_info])
         
f.close()

