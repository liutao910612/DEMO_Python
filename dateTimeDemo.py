import datetime

# today()返回一个当前本地时间的datetime对象
import time

import pytz

print("today is : ",datetime.datetime.today()) # 2020-02-18 21:24:48.838799

# now([tz]) 如果提供了参数tz，就获取tz参数所指时区的本地时间
print("now is : ",datetime.datetime.now(pytz.timezone('Asia/Shanghai'))) # 2020-02-18 21:30:37.487846+08:00

# utcnow() 返回utc时间的datetime对象
print("utcnow is : ",datetime.datetime.utcnow()) # 2020-02-18 13:33:04.378297

# fromtimestamp(timestamp[,tz]) 根据时间戳创建一个datatime对象 ， 其中tz是时区
print("fromtimestamp is : ",datetime.datetime.fromtimestamp(time.time())) # 2020-02-19 08:27:22.909740

# utcfromtimestamp(timestamp[,tz]) 根据时间戳创建一个utc的datatime对象
print("utcfromtimestamp is : ",datetime.datetime.utcfromtimestamp(time.time())) # 2020-02-19 00:27:22.909740

# strptime(date_string,format) 格式化时间字符串，而strftime(format)和strptime的用法正好相反，是将格式字符串转换为datatime对象
dt = datetime.datetime.now()
print("strptime is : ",datetime.datetime.strptime(str(dt),"%Y-%m-%d %H:%M:%S.%f")) # 2020-02-19 08:30:49.806621



