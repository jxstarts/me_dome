# coding=gbk

from multiprocessing import  Process
import os

def info(title):
    print(title)
    print("module name:",__name__)
    # �õ�������̵�id
    print("parent process:", os.getppid())
    # �õ�������̵�id
    print("process id:", os.getpid())


def f(name):
    info("function f")
    print("hello", name)

if __name__ == '__main__':
    info('main line')
    p = Process(target=f,args=('bob', ))
    p.start()
    p.join()