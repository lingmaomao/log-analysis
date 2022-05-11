#!/usr/bin/python3
import json
# Python 字典类型转换为 JSON 对象
dict={}
"""
data = {
    'no' : 1,
    'name' : 'W3CSchool',
    'url' : 'http://www.w3cschool.cn'
}
"""
data=[
    "[    7.509275] Kernel panic - not syncing: System is deadlocked on memory",
    "[    7.647275] ---[ end Kernel panic - not syncing: System is deadlocked on memory ]---",
    "[    7.486096] Kernel panic - not syncing: System is deadlocked on memory",
    "[    7.612095] ---[ end Kernel panic - not syncing: System is deadlocked on memory ]---",
    "[  189.524022] Kernel panic - not syncing: Out of memory and no killable processes...",
    "[   83.060154] Kernel panic - not syncing: Out of memory and no killable processes..."
]
dict["timeSeq"]=data
json_str = json.dumps(data)
print ("Python 原始数据：", repr(data))
print ("JSON 对象：", json_str)

with open("test.json", "w", encoding='utf-8') as f:
        # indent 超级好用，格式化保存字典，默认为None，小于0为零个空格
        f.write(json.dumps(dict, indent=4))
        # json.dump(a,f,indent=4)   # 和上面的效果一样
