# 课件下载
    - https://github.com/tulingxueyuan

# Django
- 环境
    - Python3.6
    - Django1.8
- 参考资料
    - [参考文献]：https://yiyibooks.cn
    - Django架站的16堂课
# 环境搭建
- anaconda+pycharm
- anaconda的使用
    - conda list：显示当前环境安装的包
    - conda env list：显示安装的虚拟环境列表
    - conda create -n env_name Python=3.6
    - 激活conda的虚拟环境
        - (Linux)source activate env_name
        - (win)conda activate env_name
    - pip install Django=1.8
    
# 后台需要的流程


# 创建一个Django程序
- 找到具体项目文件夹下 Django-admin startproject DjangoDome
- 启动Django
    - cd DjangoDome
    - anaconda prompt 命令行 Python manage.py runserver
- pycharm 启动
    - 需要配置
    
# 路由系统 - urls
- 创建APP
    - APP：负责一个具体业务或者一类具体业务的模块
    - Python manage.py startapp env_name

- 路由
    - 按照具体的请求url，导入到相应的业务处理模块的一个功能
    - Django的信息控制中枢
    - 本质上是接受的URL和相应的处理模块的一个映射
    - 在接受URL请求的匹配上使用了RE
    - URL的具体格式如urls.py中所示

- 需要关注两点：
    1.接受的URL是什么，即如何用RE对传入的URL进行匹配
    2.已知URL匹配到那个处理模块
    
   
- url匹配规则
    - 从上往下一个一个比对
    - url格式是分级格式，则按照级别一级一级往下比对,主要对应url包含子url的情况
    - 子url一旦被调用，则不会返回到主url
        - `/one/two/three/`
    - 正则以r开头,表示不需要转义，注意尖号(^)和美元符号($)
        - `/one/two/three` 配对 r'^one/
        - `/oo/one/two/three` 不配对 r'^one/"
        - `/one/two/three/` 配对 r'three/$'
        - `/oo/one/two/three/oo/` 不配对 r'three/$"
        - 开头不需要有反斜杠
    - 如果从上向下都没有找到合适的匹配内容，则报错
    
# 2. 正常映射
- 把某一个符合RE的URL映射到事物处理函数中去
    - 举例如下:
       '''
        from showeast import views as sv

        urlpatterns = [
            url(r'^admin/', admin.site.urls),
            url(r'^normalmap/', sv.normalmap),
        ]
       '''
# 3. URL中带参数映射
- 在事件处理代码中需要由URL传入参数,形如 /myurl/param中的param
- 参数都是字符串形式,如果需要整数等形式需要自行转换
- 通常的形式如下:
    ```
      /search/page/432 中的 432需要经常性变换，所以设置成参数比较合适
    ```        ```
    
# 4. URL在app中处理
- 如果所有应用URL都集中tulingxueyuan/urls.py中,可能导致文件的臃肿
- 可以把urls具体功能逐渐分散到每个app中
    - 从django.conf.urls 导入 include
    - 注意此时RE部分的写法
    - 添加include导入
- 使用方法
    - 确保include被导入
    - 写主路由的开头url
    - 写子路由
    - 编写views函数
- 同样可以使用参数    