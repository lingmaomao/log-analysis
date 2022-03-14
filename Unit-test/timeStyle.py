import time
#2022-01-08T09:25:57 -> 11/21/2021,10:33:59
a="2022-01-08T09:25:57"
timeArray = time.strptime(a, "%Y-%m-%dT%H:%M:%S")
print("timeArray:", timeArray)
otherStyleTime = time.strftime("%m/%d/%Y,%H:%M:%S", timeArray)
print("otherStyeTime:", otherStyleTime)