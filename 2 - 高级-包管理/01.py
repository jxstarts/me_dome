import time
import os
#包含一个学生类
#一个sayhello函数
#一个打印语句
class Student():
    def __init__(self, name="NoName", age=18):
        self.name = name
        self.age = age

    def say(self):
        print("我的名字是{0}".format(self.name))

def sayHello():
    print("你好")

#print("这里是模块一")


# 把时间表示成， 2018 9.18 11:26
# t = time.localtime()
# ft = time.strftime("%Y年%m月%d日 %H:%M:%S", t)
# print(ft)

rst = os.system("ls")
os.system("ipconfig")
print(rst)