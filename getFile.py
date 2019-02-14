import os
converted_files_dir ='/home/maomao/LOG-analysis/convert_logs'
file_names = os.listdir(converted_files_dir)
#print(file_names)
for k in range(len(file_names)):
    if file_names[k].startswith("converted_"):
        print(file_names[k])
