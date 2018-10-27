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
    