import datetime
time="2022-01-08T09:25:57"
Today= datetime.datetime.strptime(time,'%Y-%m-%dT%H:%M:%S')
#Today= datetime.datetime.today()
#Replace 100 with whatever number of time intervals you want.
print("Today:", Today)

today=Today.strftime('%Y-%m-%dT%H:%M:%S')
print("today:", today)

date_list = [Today + datetime.timedelta(seconds=x) for x in range(-60, 60)] #Finally, format the list in the way that you would like, using code like that below.
datetext=[x.strftime('%Y-%m-%dT%H:%M:%S') for x in date_list]
print(len(datetext))
print(datetext)
