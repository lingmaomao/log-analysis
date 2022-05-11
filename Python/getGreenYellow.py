
import os
#converted_files_dir ='/home/maomao/LOG-analysis/convert_logs'
converted_files_dir ='/home/maomao/LOG-analysis/0logs/'

#pattern
#1.all green
#2.green->yellow
#3.green->yellow->green->yellow

def extractComp(filename):
    file=converted_files_dir+filename;
    f = open(file,'rb')
    byt = f.readlines()
    status=0
    #print(byt)
    #for every line
    for m in range(len(byt)):
        data0=str(byt[m], 'utf-8')

        if (-1 != data0.find("Green")):
            print("data0:", data0)
            if (status==0):
                status=1
            if (status==2):
                status=3

        if (-1 != data0.find("Yellow")):
            print("data0:", data0)
            if (status==1):
                status=2
    if (status==1):
        print("filename:", filename)
    return status

file_names = os.listdir(converted_files_dir)
#print(file_names)
status1=0
status2=0
status3=0
for k in range(len(file_names)):
    if file_names[k].startswith("Tencent_"):
        print(file_names[k])
        status=extractComp(file_names[k])
        if (status==1):
            status1=status1+1;
        if (status==2):
            status2=status2+1;
        if (status==3):
            status3=status3+1;
        print(status1, status2, status3)
        #exit()
    print(status1, status2, status3)

