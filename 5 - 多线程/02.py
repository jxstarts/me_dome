
# coding=gbk
'''
利用time 函数，生成两个函数
顺序调用
计算总的 运行时间

'''

import time

def loop1():
    # ctime 得到当前时间
    print("Start loop 1 at :", time.ctime())
    # 睡眠多长时间，单位是秒
    time.sleep(4)
    print("end loop 1 at :", time.ctime())

def loop2():
    # ctime 得到当前时间
    print("Start loop 2 at :", time.ctime())
    # 睡眠多长时间，单位是秒
    time.sleep(2)
    print("end loop 2 at :", time.ctime())


def main():
    print("Starting at:", time.ctime())
    # 启动多线程的意思是用多线程去执行某个函数
    # 启动多线程函数为 start_new_thead
    # 参数两个，一个是需要运行的函数名，第二个是函数的参数作为元祖使用，为空则使用空元祖
    # 注意：如果函数只有一个参数，需要参数后有一个逗号
    print("All done at:", time.ctime())

if __name__ == '__main__':
    main()