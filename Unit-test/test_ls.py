import os
#import xlsxwriter as xw
import subprocess
import time
import datetime

#converted_files=`ls /home/maomao/LOG-analysis/convert_logs`
converted_files_dir ='/home/maomao/LOG-analysis/convert_logs'
cmd='ls ' + converted_files_dir
print("cmd: ", cmd)
files = subprocess.check_output(cmd, shell=True)
print("files: ", files)
#data=str(files, 'utf-8')
for file in files:
    print("", file)
