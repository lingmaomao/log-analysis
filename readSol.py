import csv
import os
import time
import datetime

"""
KEYS=[
    "Linux Version", #boot time,Jun 2 19:06:29 CST 2021
    "microcode", #get line
    "kernel panic", #get  line
    "Error", #get line
    "NMI" #get line
]
"""

KEYS=[
    "microcode", #get line
    "NMI" #get line
]

res_file = "sol.csv"
f = open(res_file, 'w', encoding='utf-8', newline="")
#f = open(res_file, 'w', encoding='cp936', newline="")
csv_writer = csv.writer(f)
head_text=["filename"]
head_text = head_text + KEYS 
csv_writer.writerow(head_text)

info_set=[]

def extractComp(filename, meachine):
    #f = open(filename,'rb', encoding='cp936')
    f = open(filename,'rb')
    byt = f.readlines()
    #print("byt:", byt)
    #for every line
    info_set=[]
    info_set.append(meachine)

    for k in range(len(KEYS)):
        info=""
        for m in range(len(byt)):
            #print("byt:", byt[m])
            text = byt[m].decode(errors='replace')
            #print("text:", text)
            data0=text
            #data0=str(byt[m], 'utf-8')
            if (data0.find(KEYS[k])!=-1):
                #print("Data0:", data0)
                if (KEYS[k]=="microcode"):
                    pos=data0.find("revision")
                    if (pos!=-1):
                        data=data0[pos:-1]
                        data=data.strip()
                        data=data.replace("\r\n", "")
                        data=data.replace("\t", "")
                        info=info+data
                        print("info:", info)
                        break
                else:
                    info=info+data0
                    print("info2:", info)
        print("Info:", info)
        info_set.append(info)

    print("info_set:", info_set)
    csv_writer.writerow(info_set)
    
path='/home/maomao/LOG-analysis/Error_logs/Logs/'
#path='/home/maomao/LOG-analysis/Tencent_LC22113800013_2022-01-28-16-22'
dirs=os.listdir(path)
for m in range(len(dirs)):
    filename = path+dirs[m]+'/onekeylog/runningdata/var/sollog/SOLHostCapture.log'
    #filename = path+'/onekeylog/runningdata/var/sollog/SOLHostCapture.log'
    #SOLHostCapture.log
    print("filename:", filename)
    #extractComp(filename, "dir")
    extractComp(filename, dirs[m])
    #exit()

f.close()