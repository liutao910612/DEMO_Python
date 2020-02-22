# _thread模块
import _thread
import datetime
import threading
from asyncio import sleep

date_time_format = "%y-%M-%d %H:%M:%S"


def date_time_str(date_time):
    return datetime.datetime.strftime(date_time, date_time_format)


def loop_one():
    print("--thread one start at : ", date_time_str(datetime.datetime.now()))
    print("--thread one sleep 4 seconds")
    sleep(4)
    print("--thread one end at : ", date_time_str(datetime.datetime.now()))


def loop_two():
    print("--thread two start at : ", date_time_str(datetime.datetime.now()))
    print("--thread two sleep 2 seconds")
    sleep(2)
    print("--thread two end at : ", date_time_str(datetime.datetime.now()))


def main_one():
    print("-- all threads start at : ", date_time_str(datetime.datetime.now()))
    _thread.start_new_thread(loop_one, ())
    _thread.start_new_thread(loop_two, ())
    sleep(6)
    print("-- all threads end at : ", date_time_str(datetime.datetime.now()))


# Thread 类
loops = [4, 1]


def loop(n_loop, n_sec):
    print("thread（", n_loop, "）begin to run at ：", date_time_str(datetime.datetime.now()), ",sleep（", n_sec,
          ")seconds firstly")
    sleep(n_sec)
    print("thread（", n_loop, "）end sleeping at :", date_time_str(datetime.datetime.now()))


def main_two():
    print("-- all threads start at : ", date_time_str(datetime.datetime.now()))
    threads = []
    n_loops = range(len(loops))
    for i in n_loops:
        t = threading.Thread(target=loop, args=(i, loops[i]))
        threads.append(t)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print("-- all threads end at : ", date_time_str(datetime.datetime.now()))


# The param of Thread is class object that can be called
class ThreadFunc(object):
    def __init__(self, func, args, name=''):
        self.name = name
        self.func = func
        self.args = args

    def __call__(self):
        self.func(*self.args)


def main_three():
    print("-- all threads start at : ", date_time_str(datetime.datetime.now()))
    threads = []
    n_loops = range(len(loops))
    for i in n_loops:
        t = threading.Thread(target=ThreadFunc(func=loop, args=(i, loops[i]), name=loop.__name__))
        threads.append(t)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print("-- all threads end at : ", date_time_str(datetime.datetime.now()))


# Thread async , place the control between acquire and release .
class MyThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("start thread : ", self.name)
        threading.Lock().acquire()
        print_time(self.name, self.counter, 3)
        threading.Lock().release()


def print_time(threadName, delay, counter):
    while counter:
        sleep(delay)
        print("%s :%s" % (threadName, date_time_str(datetime.datetime.now())))
        counter -= 1

def main_four():
    thread1 = MyThread(1,"Thread-1",1)
    thread2 = MyThread(2,"Thread-2",2)


    thread1.start()
    thread2.start()
    threads = [thread1, thread2]

    for thread in threads:
        thread.join()

    print("main thread complete")


if __name__ == '__main__':
    main_four()
