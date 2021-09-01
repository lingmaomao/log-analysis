#filename='/home/maomao/LOG-analysis/Error_logs/Logs/Tencent_LC2192090009A_2022-01-17-09-53/onekeylog/component/component.log'
filename='./component.log'
f = open(filename,'rb')
byt = f.readlines()
#print(byt)
#for every line

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

for m in range(len(byt)):
    data=str(byt[m], 'utf-8')
    print("data:", data)
    #exit()
    if (len(data)>=2) and (data[0]=='['):
        lists=eval(data)
        print(type(lists))
        print(lists)
        get_FW(lists)
    if (len(data)>=2) and (data[0]=='{'):
        cpu_info=get_cpu(data)
        #key="proc_name"
        #key="cpu_power"