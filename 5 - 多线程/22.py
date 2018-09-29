
# coding=gbk
import multiprocessing
from time import ctime


def consumer(input_q):
    print("Into consumer:", ctime())
    while True:
        # ������
        item = input_q.get()
        print ("pull", item, "out of q") # �˴��滻Ϊ���õĹ���
        input_q.task_done() # �����ź�֪ͨ�������
    print ("Out of consumer:", ctime()) ##�˾�δִ�У���Ϊq.join()�ռ����ĸ�task_done()�źź�������������δ�ȵ�print�˾���ɣ�����ͽ�����


def producer(sequence, output_q):
    print ("Into procuder:", ctime())
    for item in sequence:
        output_q.put(item)
        print ("put", item, "into q")
    print ("Out of procuder:", ctime())



# ��������
if __name__ == '__main__':
    q = multiprocessing.JoinableQueue()
    # ���������߽���
    cons_p = multiprocessing.Process (target = consumer, args = (q,))
    cons_p.daemon = True
    cons_p.start()

    # ��������sequence����Ҫ���͸������ߵ�������
    # ��ʵ���У���������������������ͨ��һЩ������ʽ��������
    sequence = [1,2,3,4]
    producer(sequence, q)
    # �ȴ����������
    q.join()