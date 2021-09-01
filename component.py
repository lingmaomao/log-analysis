#!/usr/bin/python3
# -*- coding: utf-8 -*-

import csv
import os
import subprocess
import time
import datetime

# 1. 
#f = open('log.csv', 'w', encoding='utf-8', newline="")
#csv_writer = csv.writer(f)


#filename = converted_files_dir + filename
filename='/home/maomao/LOG-analysis/Error_logs/Logs/Tencent_LC2192090009A_2022-01-17-09-53/onekeylog/component/component.log'
#get_data_cmd='grep ' + ' ME ' + filename + '| awk \'{print $2}\''
#get_data_cmd='grep ' + ' ME ' + filename + '| awk \'{print $2}\''
get_data_cmd='grep ' + ' "\<ME\>" ' + filename
print("get_data_cmd: ", get_data_cmd)
latency = subprocess.check_output(get_data_cmd, shell=True)
print("latency: ", latency)
data=str(latency, 'utf-8')

print ("latency[0]: ", latency[1:20])
print ("data[0]: ", data[1:20])
time=data[1:20]
