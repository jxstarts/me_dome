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
