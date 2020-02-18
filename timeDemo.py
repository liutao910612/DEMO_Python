import  time
# time模块
# time 函数，返回当前时间的时间戳(毫秒)
print(time.time())

# 格式化时间戳为本地时间的struct_time
print(time.localtime())

# UTC时区的struct_time
print(time.gmtime())

# time()和gmtime()的逆运算
print(time.mktime((2020,2,18,8,56,38,1,49,0)))

# 返回可读形式的时间字符串,注意：asctime()同时也可以接受9位元素的元组，和mktime()类似
print(time.asctime(time.localtime()))

# ctime()相当于asctime(localtime(secs))
print(time.ctime())

# sleep()用于推迟线程挂起多少秒
def test_sleep():
    print('Start :%s'%time.ctime())
    time.sleep(5)
    print('End :%s'%time.ctime())
test_sleep()


# clock()
# t1 = time.clock()
# time.sleep(2)
# print(time.clock())

# strftime(format[,t]) 返回格式化的时间字符串，其中t为可以指定的时间元组
print(time.strftime('%Y %m %d %H:%M:%S'))

#strptime(string[,format]) 以指定格式将一个时间字符串转换成时间元组
print(time.strptime("2020 02 18 21:17:00","%Y %m %d %H:%M:%S"))