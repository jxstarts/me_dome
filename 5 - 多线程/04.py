# coding=gbk
#����time��ʱ������������������
# ���ö��̵߳���
# ����������ʱ��
# ��ϰ�������Ķ��߳���������
import time
# ������̴߳����
import threading

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
    # ����threading.Threadʵ��
    t1 = threading.Thread(target=loop1, args=("���ϴ�",))
    t1.start()

    t2 = threading.Thread(target=loop2, args=("������", "��С��"))
    t2.start()

    print("All done at:", time.ctime())


if __name__ == "__main__":
    main()
    # һ��Ҫ��while���
    # ��Ϊ�������̺߳󱾳������Ϊ���̴߳���
    # ������߳�ִ����ϣ������߳̿���Ҳ��Ҫ��ֹ
    while True:
        time.sleep(10)
