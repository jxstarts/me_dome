# LOG
- https://www.cnblogs.com/yyds/p/6901864.html
- logging
- loggingģ���ṩģ�鼶��ĺ�����¼��־
- �����Ĵ����

## 1.��־��ظ���
- ��־
- ��־�ļ���level��
    - ��ͬ���û���ע��ͬ�ĳ�����Ϣ
    - DEBUG
    - INFO
    - NOTICE
    - WARNING
    - ERROR
    - CRITICAL
    - ALERT
    - EMERGENCY
- IO���� => ��ҪƵ������
- LOG������
    - ����
    - �˽�������������
    - ������λ����
- ��־��Ϣ
    - time
    - �ص�
    - level
    - ����
- ����ĵ�������־
    - log4j
    - log4php
    - logging
# 2 Loggingģ��
- ��־����
    - ������Զ���
    - DEBUG
    - INFO
    - WARNING
    - ERROR
    - CRITICAL
- ��ʼ��/д��־ʵ����Ҫָ������ֻ�е�������ڻ����ָ������ű���¼
- ʹ�÷�ʽ
    - ֱ��ʹ��logging(��װ���������)
    - Logging�Ĵ����ֱ�Ӷ���

# 2.1 Loggingģ�鼶�����־
- ʹ�����¼�������
     - logging.debug(msg, *args, **kwargs) 	����һ�����ؼ���ΪDEBUG����־��¼
     - logging.info(msg, *args, **kwargs) 	����һ�����ؼ���ΪINFO����־��¼
     - logging.warning(msg, *args, **kwargs) 	����һ�����ؼ���ΪWARNING����־��¼
     - logging.error(msg, *args, **kwargs) 	����һ�����ؼ���ΪERROR����־��¼
     - logging.critical(msg, *args, **kwargs) 	����һ�����ؼ���ΪCRITICAL����־��¼
     - logging.log(level, *args, **kwargs) 	����һ�����ؼ���Ϊlevel����־��¼
     - logging.basicConfig(**kwargs) 	��root logger����һ��������
- logging.basicConfig(**kwargs) 	��root logger����һ��������
    - ֻ�ڵ�һ�ε��õ�ʱ��������
    - ������logger��ʹ��Ĭ��ֵ
        - �����sys.stderr
        - ����WARNING
        - ��ʽ��level��log_name:content
- ����01
- format����
        
                asctime 	%(asctime)s 	��־�¼�������ʱ��--����ɶ�ʱ�䣬�磺2003-07-08 16:49:45,896
                created 	%(created)f 	��־�¼�������ʱ��--ʱ��������ǵ�ʱ����time.time()�������ص�ֵ
                relativeCreated 	%(relativeCreated)d 	��־�¼�������ʱ�������loggingģ�����ʱ�����Ժ�������Ŀǰ����֪�������õģ�
                msecs 	%(msecs)d 	��־�¼������¼��ĺ��벿��
                levelname 	%(levelname)s 	����־��¼��������ʽ����־����'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'��
                levelno 	%(levelno)s 	����־��¼��������ʽ����־����10, 20, 30, 40, 50��
                name 	%(name)s 	��ʹ�õ���־�����ƣ�Ĭ����'root'����ΪĬ��ʹ�õ��� rootLogger
                message 	%(message)s 	��־��¼���ı����ݣ�ͨ�� msg % args����õ���
                pathname 	%(pathname)s 	������־��¼������Դ���ļ���ȫ·��
                filename 	%(filename)s 	pathname���ļ������֣������ļ���׺
                module 	%(module)s 	filename�����Ʋ��֣���������׺
                lineno 	%(lineno)d 	������־��¼������Դ�������ڵ��к�
                funcName 	%(funcName)s 	������־��¼�����ĺ�����
                process 	%(process)d 	����ID
                processName 	%(processName)s 	�������ƣ�Python 3.1����
                thread 	%(thread)d 	�߳�ID
                threadName 	%(thread)s 	�߳����� 
# 2.2 loggingģ��Ĵ�������
- �Ĵ����
    - ��־����Logger��:������־��һ���ӿ�
    - ��������Handler�����Ѳ�������־���͵���Ӧ��Ŀ�ĵ�
    - ��������Filter��������ϸ������Щ��־���
    - ��ʽ����Formatter�������������Ϣ��ʽ��
- logger
    - ����һ����־
    - ����
           Logger.setLevel() 	������־�����ᴦ�����־��Ϣ��������ؼ���
           Logger.addHandler() �� Logger.removeHandler() 	Ϊ��logger������� �� �Ƴ�һ��handler����
           Logger.addFilter() �� Logger.removeFilter() 	Ϊ��logger������� �� �Ƴ�һ��filter����
           Logger.debug: ����һ��debug�������־��ͬ��info��error����
           Logger.exception(): ����������Logger.error����־��Ϣ
           Logger.log():��ȡһ����ȷ����־level�����ഴ��һ����־��¼
    
    - ��εõ�һ��logger����
        - ʵ����
        - logging.getLogger()
- Handler
    - ��log���͵�ָ��λ��
    - ����
        - setLevel
        - setFormat
        - addFilter��removeFilter
    - ����Ҫֱ��ʹ�ã�Handler�ǻ���
            logging.StreamHandler 	����־��Ϣ���͵������Stream����std.out, std.err���κ�file-like����
            logging.FileHandler 	����־��Ϣ���͵������ļ���Ĭ��������ļ���С����������
            logging.handlers.RotatingFileHandler 	����־��Ϣ���͵������ļ�����֧����־�ļ�����С�и�
            logging.hanlders.TimedRotatingFileHandler 	����־��Ϣ���͵������ļ�����֧����־�ļ���ʱ���и�
            logging.handlers.HTTPHandler 	����־��Ϣ��GET��POST�ķ�ʽ���͸�һ��HTTP������
            logging.handlers.SMTPHandler 	����־��Ϣ���͸�һ��ָ����email��ַ
            logging.NullHandler 	��Handlerʵ�������error messages��ͨ������ʹ��logging��library������ʹ��������'No handlers could be found for logger XXX'��Ϣ�ĳ��֡�

- format��
    - ֱ��ʵ����
    - ���Լ̳�Format�����������
    - ��������
        - fmt��ָ����Ϣ��ʽ���ַ����������ָ���ò�����Ĭ��ʹ��message��ԭʼֵ
        - datefmt��ָ�����ڸ�ʽ�ַ����������ָ���ò�����Ĭ��ʹ��"%Y-%m-%d %H:%M:%S"
        - style��Python 3.2�����Ĳ�������ȡֵΪ '%', '{'�� '$'�������ָ���ò�����Ĭ��ʹ��'%'   
 - filter��
    - ���Ա�Handler��Loggerʹ��
    - ���ƴ��ݹ�������Ϣ�ľ�������
    - ����02          