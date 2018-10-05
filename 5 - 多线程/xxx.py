# coding=gbk

# ����v04�� ί��������
from collections import namedtuple

'''
���ͣ�
1. ��� for ѭ��ÿ�ε������½�һ�� grouper ʵ������ֵ�� coroutine ������ grouper ��ί����
������

2. ���� next(coroutine)��Ԥ��ί�������� grouper����ʱ���� while True ѭ���������������� 
averager ���� yield from ���ʽ����ͣ��

3. �ڲ� for ѭ������ coroutine.send(value)��ֱ�Ӱ�ֵ������������ averager��ͬʱ����ǰ�� 
grouper ʵ����coroutine���� yield from ���ʽ����ͣ��

4. �ڲ�ѭ�������� grouper ʵ�������� yield from ���ʽ����ͣ����ˣ� grouper��������
����Ϊ results[key] ��ֵ����仹û��ִ�С�

5. coroutine.send(None) ��ֹ averager �������������������׳� StopIteration �쳣������
�ص����ݰ������쳣�����value�У�yield from ����ֱ��ץȡ StopItration �쳣�����쳣����
�� value ��ֵ�� results[key]
'''
ResClass = namedtuple('Res', 'count average')


# ��������
def averager():
    total = 0.0
    count = 0
    average = None

    while True:
        term = yield
        # None���ڱ�ֵ
        if term is None:
            break
        total += term
        count += 1
        average = total / count

    return ResClass(count, average)


# ί��������
def grouper(storages, key):
    while True:
        # ��ȡaverager()���ص�ֵ
        storages[key] = yield from averager()


# �ͻ��˴���
def client():
    process_data = {
        'boys_2': [39.0, 40.8, 43.2, 40.8, 43.1, 38.6, 41.4, 40.6, 36.3],
        'boys_1': [1.38, 1.5, 1.32, 1.25, 1.37, 1.48, 1.25, 1.49, 1.46]
    }

    storages = {}
    for k, v in process_data.items():
        # ���Э��
        coroutine = grouper(storages, k)

        # Ԥ��Э��
        next(coroutine)

        # �������ݵ�Э��
        for dt in v:
            coroutine.send(dt)

        # ��ֹЭ��
        coroutine.send(None)
    print(storages)

# run
client()