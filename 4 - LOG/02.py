# coding=gbk
'''

1. ����

���������¼�����־��¼������

    1��Ҫ�����м����������־��д������ļ���
    2��all.log�ļ��м�¼���е���־��Ϣ����־��ʽΪ�����ں�ʱ�� - ��־���� - ��־��Ϣ
    3��error.log�ļ��е�����¼error�����ϼ������־��Ϣ����־��ʽΪ�����ں�ʱ�� - ��־���� - �ļ���[:�к�] - ��־��Ϣ
    4��Ҫ��all.log��ÿ���賿������־�и�

2. ����

    1��Ҫ��¼���м������־�������־������Чlevel��Ҫ����Ϊ��ͼ���--DEBUG;
    2����־��Ҫ�����͵�������ͬ��Ŀ�ĵأ������ҪΪ��־����������handler�����⣬����Ŀ�ĵض��Ǵ����ļ������������handler������FileHandler��صģ�
    3��all.logҪ����ʱ�������־�и�������Ҫ��logging.handlers.TimedRotatingFileHandler; ��error.logû��Ҫ����־�и��˿���ʹ��FileHandler;
    4��������־�ļ��ĸ�ʽ��ͬ�������Ҫ��������handler�ֱ����ø�ʽ����
'''


import logging
import logging.handlers
import datetime


# ���� logger
logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)


#Ϊ������ͬ���ļ����ò�ͬ��handler
rf_handler = logging.handlers.TimedRotatingFileHandler('all.log', when='midnight', interval=1, backupCount=7, atTime=datetime.time(0, 0, 0, 0))
rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))



f_handler = logging.FileHandler('error.log')
f_handler.setLevel(logging.ERROR)
f_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))

# ����Ӧ�Ĵ�������װ��logger��
logger.addHandler(rf_handler)
logger.addHandler(f_handler)


logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')