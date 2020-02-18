import datetime

# today()返回一个当前本地时间的datetime对象
import pytz

print("today is : ",datetime.datetime.today()) # 2020-02-18 21:24:48.838799

# now([tz]) 如果提供了参数tz，就获取tz参数所指时区的本地时间
print("now is : ",datetime.datetime.now(pytz.timezone('Asia/Shanghai'))) # 2020-02-18 21:30:37.487846+08:00

# utcnow() 返回utc时间的datetime对象
print("utcnow is : ",datetime.datetime.utcnow()) # 2020-02-18 13:33:04.378297


