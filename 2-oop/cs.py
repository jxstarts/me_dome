# peroperty案例
# 定义一个Person类，具有name，age属性
# 对于任意输入的香茗，希望都用大写方式保存
# 年龄，希望内部统一证书保存
# property(fget, fset, fdel, doc)
class Person():

    # 函数民称任意
    def fget(self):
        return self._name * 2

    def fset(self, name):
        # 所输入的name以大写形式保存
        self._name = name.upper()

    def fdel(self):
        self._name = "NoName"

    name = property(fget, fset, fdel, "对name进行操作")


p1 = Person()
p1.name = "aa"
print(p1.name)