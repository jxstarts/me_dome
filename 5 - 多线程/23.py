# coding=gbk
import multiprocessing
from time import ctime

# �����ڱ�����
def consumer(input_q):
    print("Into consumer:", ctime())
    while True:
        item = input_q.get()
        if item is None:
            break
        print("pull", item, "out of q")
    print ("Out of consumer:", ctime()) ## �˾�ִ����ɣ���ת��������


def producer(sequence, output_q):
    print ("Into procuder:", ctime())
    for item in sequence:
        output_q.put(item)
        print ("put", item, "into q")
    print ("Out of procuder:", ctime())

if __name__ == '__main__':
    q = multiprocessing.Queue()
    cons_p = multiprocessing.Process(target = consumer, args = (q,))
    cons_p.start()

    sequence = [1,2,3,4]
    producer(sequence, q)

    q.put(None)
    cons_p.join()