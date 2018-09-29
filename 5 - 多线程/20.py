# coding=gbk

import multiprocessing
from time import sleep, ctime

class ClockProcess(multiprocessing.Process):
    '''
    ���������Ƚ���Ҫ
    1.init���캯��
    2.run
    '''

    def __init__(self, interval):
        super().__init__()
        self.interval = interval

    def run(self):
        while True:
            print("���ڵ�ʱ���� %s" % ctime())
            sleep(self.interval)

if __name__ == '__main__':
    p = ClockProcess(3)
    p.start()
    #
    # while True:
    #     print()
    #     sleep(1)