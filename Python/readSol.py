import csv
import os
import time
import datetime

path='/home/maomao/LOG-analysis/Error_logs/Logs/'

KEYS=[
    "Linux version",#boot time,Jun 2 19:06:29 CST 2021
    "microcode", #get line
    "Kernel panic", #get  line
    " Error", #get line
    "NMI" #get line
]

res_file = "sol.csv"
f = open(res_file, 'w', encoding='utf-8', newline="")
csv_writer = csv.writer(f)
head_text=["filename"]
head_text = head_text + KEYS 
csv_writer.writerow(head_text)

info_set=[]

def extractComp(filename, meachine):
    f = open(filename,'rb')
    byt = f.readlines()
    info_set=[]
    info_set.append(meachine)

    for k in range(len(KEYS)):
        info=""
        for m in range(len(byt)):
            text = byt[m].decode(errors='replace')
            data0=text
            if (data0.find(KEYS[k])!=-1):
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
                    if (len(data0)<180 or (KEYS[k]!=" Error" and KEYS[k]!="Linux version")):
                        if (KEYS[k]=="Linux version"):
                            pos = data0.find("SMP")
                            prefix_lens=len("SMP Fri")
                            data0=data0[pos+prefix_lens:-1]
                        info=info+data0
                        print("info2:", info)
        #print("Info:", info)
        info_set.append(info)

    #print("info_set:", info_set)
    csv_writer.writerow(info_set)
    
dirs=os.listdir(path)
for m in range(len(dirs)):
    filename = path + dirs[m] + '/onekeylog/runningdata/var/sollog/SOLHostCapture.log'
    print("filename:", filename)
    extractComp(filename, dirs[m])

f.close()