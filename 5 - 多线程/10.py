# coding=gbk
import threading
from time import sleep, ctime


loop = [4,2]

class ThreadFunc:

    def __init__(self, name):
        self.name = name

    def loop(self, nloop, nsec):
        '''
        :param nloop: loop����������
        :param nsec: ϵͳ����ʱ��
        :return:
        '''
        print('Start loop ', nloop, 'at ', ctime())
        sleep(nsec)
        print('Done loop ', nloop, ' at ', ctime())

def main():
    print("Starting at: ", ctime())

    # ThreadFunc("loop").loop ��һ������ʽ����ȣ�
    # t = ThreadFunc("loop")
    # t.loop
    # ����t1 ��  t2�Ķ��巽ʽ���
    t = ThreadFunc("loop")
    t1 = threading.Thread( target = t.loop, args=("LOOP1", 4))
    # ��������д���������ˣ���ҵ��һ��
    t2 = threading.Thread( target = ThreadFunc('loop').loop, args=("LOOP2", 2))

    # ��������д��
    #t1 = threading.Thread(target=ThreadFunc('loop').loop(100,4))
    #t2 = threading.Thread(target=ThreadFunc('loop').loop(100,2))

    t1.start()
    t2.start()

    t1.join( )
    t2.join()


    print("ALL done at: ", ctime())


if __name__ == '__main__':
    main()