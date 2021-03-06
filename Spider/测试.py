# coding=gbk
import requests #导入需要的包
import json

search = input("请输入你要翻译的内容:")

url = "https://fanyi.baidu.com/extendtrans" #请求的地址
headers={"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36"} #设置请求的头部

#设置提交的数据
posData={"query":search,
                "from":"en",
                "to":"zh"}

response = requests.post(url=url,data=posData,headers=headers)#模拟请求

#获取response的数据有2种方式 一种是text获取的直接是文本格式 但是可能有乱码 需要手动设置response.encoding("编码") 解决乱码
#还有一种就是response.content 里面存的是网站直接返回的数据 二进制格式 然后通过decode解码即可
#因为返回的是json对象，所以我们将最后解码后的字符串进行json格式转换 使用json.loads()进行转换
json_data=json.loads(response.content.decode())

#然后我们可以通过格式化工具进行json的解析
print("单词:{0} 翻译:{1}".format(search,json_data["data"]["st_tag"]))