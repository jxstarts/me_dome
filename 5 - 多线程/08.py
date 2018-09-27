# coding=gbk
import time
import threading

def loop1():
    # ctime �õ���ǰʱ��
    print('Start loop 1 at :', time.ctime())
    # ˯�߶೤ʱ�䣬��λ����
    time.sleep(6)
    print('End loop 1 at:', time.ctime())

def loop2():
    # ctime �õ���ǰʱ��
    print('Start loop 2 at :', time.ctime())
    # ˯�߶೤ʱ�䣬��λ����
    time.sleep(1)
    print('End loop 2 at:', time.ctime())


def loop3():
    # ctime �õ���ǰʱ��
    print('Start loop 3 at :', time.ctime())
    # ˯�߶೤ʱ�䣬��λ����
    time.sleep(5)
    print('End loop 3 at:', time.ctime())

def main():
    print("Starting at:", time.ctime())
    # ����threading.Threadʵ��
    t1 = threading.Thread(target=loop1, args=( ))
    # setName�Ǹ�ÿһ�����߳�����һ������
    t1.setName("THR_1")
    t1.start()

    t2 = threading.Thread(target=loop2, args=( ))
    t2.setName("THR_2")
    t2.start()

    t3 = threading.Thread(target=loop3, args=( ))
    t3.setName("THR_3")
    t3.start()

    # Ԥ��3���thread2�Ѿ��Զ�������
    time.sleep(3)
    # enumerate �õ������������̣߳������߳�1�����߳�3
    for thr in threading.enumerate():
        # getName�ܹ��õ��̵߳�����
        print("�������е��߳������ǣ� {0}".format(thr.getName()))

    print("�������е����߳�����Ϊ�� {0}".format(threading.activeCount()))

    print("All done at:", time.ctime())

if __name__ == "__main__":
    main()
    # һ��Ҫ��while���
    # ��Ϊ�������̺߳󱾳������Ϊ���̴߳���
    # ������߳�ִ����ϣ������߳̿���Ҳ��Ҫ��ֹ
    while True:
        time.sleep(10)
