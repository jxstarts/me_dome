# coding=gbk
import time
import threading

def fun():
    print("Start fun")
    time.sleep(2)
    print("end fun")

print("Main thread")

t1 = threading.Thread(target=fun, args=() )
# ����ػ��̵߳ķ�����������start֮ǰ���ã�������Ч
t1.setDaemon(True)
#t1.daemon = True
t1.start()

time.sleep(1)
print("Main thread end")
