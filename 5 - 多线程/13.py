# coding=gbk
import threading
import time

# Python2
# from Queue import Queue

# Python3
import queue

class Producer(threading.Thread):
    def run(self):
        global queue
        count = 0
        while True:
            # qsize ���� queue���ݳ���
            if queue.qsize() < 1000:
                for i in range(100):
                    count = count + 1
                    msg = '���ɲ�Ʒ'+str(count)
                    # put ���� queue�з���һ��ֵ
                    queue.put(msg)
                    print(msg)
            time.sleep(0.5)
class Consumer(threading.Thread):
    def run(self):
        global queue
        while True:
            if queue.qsize() > 100:
                for i in range(3):
                    # get���Ǵ�queue��ȡ��һ��ֵ
                    msg = self.name + '������' + queue.get()
                    print(msg)
            time.sleep(1)

if __name__ == '__main__':
    queue = queue.Queue()
    for i in range(500):
        queue.put('��ʼ��Ʒ'+str(i))
    for i in  range(2):
        p = Producer()
        p.start()
    for i in range(5):
        c = Consumer()
        c.start()
