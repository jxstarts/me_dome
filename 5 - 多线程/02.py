
# coding=gbk
'''
����time ������������������
˳�����
�����ܵ� ����ʱ��

'''

import time
import _thread as thread
import threading

def loop1():
    # ctime �õ���ǰʱ��
    print("Start loop 1 at :", time.ctime())
    # ˯�߶೤ʱ�䣬��λ����
    time.sleep(4)
    print("end loop 1 at :", time.ctime())

def loop2():
    # ctime �õ���ǰʱ��
    print("Start loop 2 at :", time.ctime())
    # ˯�߶೤ʱ�䣬��λ����
    time.sleep(2)
    print("end loop 2 at :", time.ctime())


def main():
    print("Starting at:", time.ctime())
    # �������̵߳���˼���ö��߳�ȥִ��ĳ������
    # �������̺߳���Ϊ start_new_thead
    # ����������һ������Ҫ���еĺ��������ڶ����Ǻ����Ĳ�����ΪԪ��ʹ�ã�Ϊ����ʹ�ÿ�Ԫ��
    # ע�⣺�������ֻ��һ����������Ҫ��������һ������
    thread.start_new_thread(loop1, ())
    thread.start_new_thread(loop2, ())

    print("All done at:", time.ctime())

if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)