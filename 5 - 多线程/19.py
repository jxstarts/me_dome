# coding=gbk
import multiprocessing
from time import sleep,ctime

def clock(interval):
    while True:
        print("现在的时间是 %s" % ctime())
        sleep(interval)

if __name__ == '__main__':
    p = multiprocessing.Process(target=clock, args=(5, ))
    p.start()

    # while True:
    #     print("睡")
    #     sleep(1)