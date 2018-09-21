def SayHello(name):
    print("我叫{0}".format(name))
    print("你好{0}".format(name))
    print("``````````````````````````")

if __name__ == '__main__':
    print("***" * 20)
    name = input("请输入你的名字:")
    print(SayHello(name=name))
    print("hhhh" * 25)

