# coding=gbk

#����time��ʱ������������������
# ���ö��̵߳���
# ����������ʱ��
# ��ϰ�������Ķ��߳���������
import time
# ������̰߳�������Ϊthread
import _thread as thread

def loop1(in1):
    # ctime �õ���ǰʱ��
    print('Start loop 1 at :', time.ctime())
    # �Ѳ�����ӡ����
    print("���ǲ��� ",in1)
    # ˯�߶೤ʱ�䣬��λ����
    time.sleep(4)
    print('End loop 1 at:', time.ctime())

def loop2(in1, in2):
    # ctime �õ���ǰʱ��
    print('Start loop 2 at :', time.ctime())
    # �Ѳ���in �� in2��ӡ����������ʹ��
    print("���ǲ��� " ,in1 , "�Ͳ���  ", in2)
    # ˯�߶೤ʱ�䣬��λ����
    time.sleep(2)
    print('End loop 2 at:', time.ctime())



def main():
    print("Starting at:", time.ctime())
    # �������̵߳���˼���ö��߳�ȥִ��ĳ������
    # �������̺߳���Ϊstart_new_thead
    # ����������һ������Ҫ���еĺ��������ڶ��Ǻ����Ĳ�����ΪԪ��ʹ�ã�Ϊ����ʹ�ÿ�Ԫ��
    # ע�⣺�������ֻ��һ����������Ҫ��������һ������
    thread.start_new_thread(loop1,("���ϴ�", ))

    thread.start_new_thread(loop2,("������", "������"))

    print("All done at:", time.ctime())

if __name__ == "__main__":
    main()
    # һ��Ҫ��while���
    # ��Ϊ�������̺߳󱾳������Ϊ���̴߳���
    # ������߳�ִ����ϣ������߳̿���Ҳ��Ҫ��ֹ
    while True:
        time.sleep(10)
