import csv
import os
import time
import datetime

temperature_key=[
"Tririver,RTCInlet,Q66:",
"Tririver,OCPInlet,Q67:",
"Tririver,MBInlet,U46:",
"Tririver,outlet,Q25:",
"Tririver,outlet2,U158:",
"Tririver,inlet,J60 or Right_Ear or Left_Ear:",
"Tririver,inlet,J60",
"Tririver,inlet,Left_Ear",
"Tririver,inlet,Right_Ear",
"Tririver,PSU0_INLET",
"Tririver,PSU0_TEMP1",
"Tririver,PSU0_TEMP2",
"Tririver,PSU1_INLET",
"Tririver,PSU1_TEMP1",
"Tririver,PSU1_TEMP2",
"CPU0_DTS =",
"CPU1_DTS =",
"CPU0,MEM_VR_PVDDQ1:",
"CPU0,MEM_VR_PVPP1:",
"CPU0,MEM_VR_PVDDQ2:",
"CPU0,MEM_VR_PVPP2:",
"CPU1,MEM_VR_PVDDQ1:",
"CPU1,MEM_VR_PVPP1:",
"CPU1,MEM_VR_PVDDQ2:",
"CPU1,MEM_VR_PVPP2:"
]

res_file = "temperature.csv"
f = open(res_file, 'w', encoding='utf-8', newline="")
csv_writer = csv.writer(f)
head_text=["filename"]
head_text = head_text + temperature_key
csv_writer.writerow(head_text)

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
def extractComp(filename, meachine):
    f = open(filename,'rb')
    byt = f.readlines()
    #print(byt)
    #for every line
    head=[]
    head.append(meachine)
    for m in range(len(byt)):
        data0=str(byt[m], 'utf-8')
        for n in range(len(temperature_key)):
            key = temperature_key[n]
            #print("key:", key)
            #print("pos:", data0.find(key))
            if (data0.find(key)!=-1):
                print("Key:", key)
                print("Data0:", data0)

            data0=data0.strip()
            if (data0.find(key)!=-1 and len(data0)<len(key)+15):
                temperature=data0.replace(key, "")
                temperature=temperature.strip()
                temperature=temperature.replace("\n", "")
                temperature=temperature.replace("\t", "")
                print("temperature:", temperature)
                print("key:", key)
                print("data0:", data0)
                head.append(temperature)

    print("info:", head)
    csv_writer.writerow(head)
    
path='/home/maomao/LOG-analysis/Error_logs/Logs/'
for k in range(len(files)):
    #print(files[k])
    dirs=os.listdir(path)
    #print("dirs:", dirs)
    for m in range(len(dirs)):
        if (dirs[m].find(files[k])!=-1):
            #print("dir:", dirs[m])
            #print("file:", files[k])
            #print("m:", m)
            #print("k:", k)

            #filename = path+dirs[m]+'/onekeylog/component/component.log'
            filename = path+dirs[m]+'/onekeylog/runningdata/temperatureinfo.log'
            print("filename:", filename)
            extractComp(filename, dirs[m])
            #exit()

f.close()