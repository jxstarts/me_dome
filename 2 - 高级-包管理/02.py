#借助于importlib包可以事项导入艺术字开头的名称的模块
import importlib
#相当于导入了一个叫01的模块并把导入的模块赋值给了bao
bao = importlib.import_module("01")


stu = bao.Student()
stu.say()
