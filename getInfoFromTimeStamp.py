#!/usr/bin/python3
# -*- coding: utf-8 -*-

import csv
import os
import subprocess
import time
import datetime

logs=["idl.log", "selelist.csv", "maintenance.log"]
#logs=["idl.log", "maintenance.log"]
converted_files_dir ='/home/maomao/LOG-analysis/convert_logs/'
logs_dir="/home/maomao/LOG-analysis/Error_logs/"

def generateLog(filename):
    prefix="converted_"
    name_slice=filename.split('_')
    print("name_slice:", name_slice)
    json_file = converted_files_dir + filename
    #json_file='/home/maomao/LOG-analysis/converted_Tencent_FX21B050001PD_2022-01-17-09-55_RegRawData_1.json';
    #print("json_file:", json_file)
    log_dir = logs_dir + name_slice[1] + '_' + name_slice[2] + '_' + name_slice[3] + "/onekeylog/log/"
    print("log_dir:", log_dir)
    get_data_cmd='grep ' + 'timestamp '+ json_file + '| awk \'{print $2}\''
    print("get_data_cmd: ", get_data_cmd)
    latency = subprocess.check_output(get_data_cmd, shell=True)
    print("latency: ", latency)
    data=str(latency, 'utf-8')

    print ("latency[0]: ", latency[1:20])
    print ("data[0]: ", data[1:20])
    time_stamp=data[1:20]
    csv_writer.writerow([time_stamp])
    #2022-01-08T09:25:57

    Today= datetime.datetime.strptime(time_stamp,'%Y-%m-%dT%H:%M:%S')
    #Today= datetime.datetime.today()
    #Replace 100 with whatever number of time intervals you want.
    print("Today:", Today)

    date_list = [Today + datetime.timedelta(seconds=x) for x in range(-60, 60)] 
    #format the list in the way that you would like
    datetexts=[x.strftime('%Y-%m-%dT%H:%M:%S') for x in date_list]
    #print(len(datetext))
    #print(datetext)

    #one min before and after
    for m in range(len(datetexts)):
        time_stamp=datetexts[m]
    
        #2.extract info use timeStamp
        #get log_dir
        for l in range(len(logs)):
            if l == 1:
                #2022-01-08T09:25:57 -> 11/21/2021,10:33:59
                timeArray = time.strptime(time_stamp, "%Y-%m-%dT%H:%M:%S")
                print("timeArray:", timeArray)
                time_stamp1 = time.strftime("%m/%d/%Y,%H:%M:%S", timeArray)
                print("otherStyeTime:", time_stamp1)
 
            print("log-type: ", logs[l])
            #get_data_cmd='grep ' + time_stamp + ' /home/maomao/LOG-analysis/onekeylog/log/ -rn' + '| grep '+ logs[l]
            if l == 1:
                get_data_cmd='grep ' + time_stamp1 + ' ' + log_dir + ' -rn' + '| grep '+ logs[l]
            else:
                get_data_cmd='grep ' + time_stamp + ' ' + log_dir + ' -rn' + '| grep '+ logs[l]
            print("get_data_cmd: ", get_data_cmd)
            #grep 2022-01-08T09:25:57  -rn | grep idl
 
            status = "true"
            try:
                latency = subprocess.check_output(get_data_cmd, shell=True)
            except subprocess.CalledProcessError as e:
                latency = e.output       # Output generated before error
                code    = e.returncode   # Return code
                status  = "false"
 
            if status == "false":
                continue
 
            data=str(latency, 'utf-8')
            print("data: ", data)
            data.rstrip('\n')
            print("data.rstrip(): ", data)
        
            #ldl.log
            if l == 0:
                #<162>  2022-01-08T09:25:57.520032+08:00 FX21B050001PD InspurDiagnose:   |2022-01-08T09:25:57+08:00|MAINBOARD|Assert|Critical|12FF0202|System_Error SYS       Error  IERR  FM_CPU_MSMI_LVT3_N_Long.|
                start=data.find('|')
                Diagnose_info=data[start:]
                print("Diagnose_info:", Diagnose_info)
        
                data_slice=data.split(' ')
                print("data_slice:", data_slice)
                print("data_slice[3]:", data_slice[3])
                print("data_slice[4]:", data_slice[4])
                meachine=data_slice[3]
                InspurDiagnose=data_slice[4]
                Diagnose_info=InspurDiagnose+Diagnose_info
                csv_writer.writerow([time_stamp, logs[l], Diagnose_info])
 
            #selelist.csv
            #01/08/2022,09:25:57
            if l == 1:
                #e,11/21/2021,18:46:04,System Boot Initiated BIOS_Boot_Up,State Asserted
                #start=data.find(',')
                #Diagnose_info=data[start:]
                #print("Diagnose_info:", Diagnose_info)
        
                data_slice=data.split(',')
                print("data_slice:", data_slice)
                print("data_slice[2]:", data_slice[2])
                print("data_slice[3]:", data_slice[3])
                Diagnose_info=data_slice[3:]
                print("Diagnose_info:", Diagnose_info)
                csv_writer.writerow([time_stamp, logs[l], Diagnose_info])
 
            #maintenance.log
            if l == 2:
                #<182>  2021-11-21T09:51:18.650000+08:00 FX21B050001PD inspur_component_app:  [2194 : 2194 INFO]prepare : read pcie asset info from EEPROM
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
                    Diagnose_info=InspurDiagnose+Diagnose_info
                    csv_writer.writerow([time_stamp,logs[l], Diagnose_info])



#cmd='./test-run1.sh '+str(empu_num[l]) + ' ' + str(batch[k1])
#grep "timestamp" converted_Tencent_FX21B050001PD_2022-01-17-09-55_RegRawData_1.json | awk '{print $2}'

#1.get timeStamp

file_names = os.listdir(converted_files_dir)
#print(file_names)
for k in range(len(file_names)):
    if file_names[k].startswith("converted_"):
        print("File:", file_names[k])
        #1. 
        res_file = file_names[k]+".csv"
        f = open(res_file, 'w', encoding='utf-8', newline="")
        csv_writer = csv.writer(f)

        generateLog(file_names[k])

        f.close()
        #exit()

         

