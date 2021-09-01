import csv
import os
import subprocess
import time
import datetime


#FW Version – BMC/ BIOS / ME / CPLD / PSU

def get_cpu(data):
    key="processors"
    list=eval(data)
    print(type(list))
    print(list)
    #print("list[key]:", list[key])
    #if key in list:
    if list.get(key) is not None:
        print("############################################")
        print("list[key]:", list[key])
        sub_key="proc_name"
        if list[key][0].get(sub_key) is not None:
            print("list[key][sub_key]:", list[key][0][sub_key])
        return list[key][0][sub_key]
    else:
        return ""

#FW Version – BMC/ BIOS / ME / CPLD / PSU
fw_device=["BMC", "BIOS", "ME", "CPLD", "PSU"]
#{ 'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
fw_device_info = {"BMC": "", "BIOS":"", "ME":"", "CPLD":"", "PSU":""}
def get_FW(datas):
    for m in range(len(datas)):
        data=datas[m]
        print("data", data)
        key="dev_name"
        if data.get(key) is not None:
            for n in range(len(fw_device)):
                #print("data[key]:", data[key])
                if data.get(key)==fw_device[n]:
                    sub_key="dev_version"
                    if data.get(sub_key) is not None:
                        print("data[sub_key]:", data[sub_key])
                        fw_device_info[fw_device[n]] = data[sub_key]
    if (len(fw_device_info["ME"])>0):
        print("fw_device_info:", fw_device_info)
 
def get_cpu_info(data):
    info_list = []
    print("cpu Data", data)
    key="processors"
    if data.get(key) is not None:
        sub_key="proc_name"
        device0=data[key][0]
        if device0.get(sub_key) is not None:
            print("data[key][sub_key]:", device0[sub_key])
            info = device0[sub_key]
            info_list.append(info)
    return info_list

def get_seq_FW(datas):
    info_list = []
    for m in range(len(datas)):
        data=datas[m]
        print("data", data)
        key="dev_name"
        if data.get(key) is not None:
            sub_key="dev_version"
            if data.get(sub_key) is not None:
                print("data[sub_key]:", data[sub_key])
                #fw_device_info[fw_device[n]] = data[sub_key]
                info = data[key] + ":" + data[sub_key]
                info_list.append(info)
    return info_list

res_file = "component.csv"
f = open(res_file, 'w', encoding='utf-8', newline="")
csv_writer = csv.writer(f)

"""
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
"""
files=[
"LC21B29900015",
"X21A260008A2"
]

#HW SKU – CPU/PPIN/Memory info
def extractComp(filename):
    f = open(filename,'rb')
    byt = f.readlines()
    #print(byt)
    #for every line
    head=[]
    head.append(filename)
    info=head
    for m in range(len(byt)):
        data0=str(byt[m], 'utf-8')
        print("data0:", data0)
        if m+1==len(byt):
            continue
        data=str(byt[m+1], 'utf-8')
        #exit()
        if (len(data)>=2) and (data[0]=='['):
            lists=eval(data)
            #print(type(lists))
            #print(lists)
            if 'RESTful version info:' in data0:
                print("get_seq_FW:\n")
                fw_device_seq_info = get_seq_FW(lists)
                info = info+fw_device_seq_info
                #csv_writer.writerow(info)

        if (len(data)>=2) and (data[0]=='{'):
            lists=eval(data)
            #print(type(lists))
            #print(lists)
            if 'RESTful CPU info:' in data0:
                print("get_cpu_info:\n")
                cpu_info = get_cpu_info(lists)
                info = info+cpu_info
            #cpu_info=get_cpu(data)
            #key="proc_name"
        #key="cpu_power"
    print("info:", info)
    csv_writer.writerow(info)

    
path='/home/maomao/LOG-analysis/Error_logs/Logs/'
for k in range(len(files)):
    print(files[k])
    #filename='/home/maomao/LOG-analysis/Error_logs/Logs/Tencent_LC2192090009A_2022-01-17-09-53/onekeylog/component/component.log'
    #filename='./component.log'
    dirs=os.listdir(path)
    print("dirs:", dirs)
    for m in range(len(dirs)):
        if (dirs[m].find(files[k])!=-1):
            #print("dir:", dirs[m])
            #print("file:", files[k])
            #print("m:", m)
            #print("k:", k)

            filename = path+dirs[m]+'/onekeylog/component/component.log'
            print("filename:", filename)
            extractComp(filename)

f.close()