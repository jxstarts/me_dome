# coding=gbk
import json

# ��ʱstudent��һ��dict��ʽ���ݣ�����json
student={
    "name": "luidana",
    "age": 18,
    "mobile":"15578875040"
}

print(type(student))

stu_json = json.dumps(student)
print(type(stu_json))
print("JSON����:{0}".format(stu_json))

stu_dict = json.loads(stu_json)
print(type(stu_dict))
print(stu_dict)