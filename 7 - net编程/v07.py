# coding=gbk
# ������Ӧ�İ�
import smtplib
from email.mime.text import MIMEText
# MIMEText������Ҫ����
# 1. �ʼ�����
# 2. MIME�����ͣ��ڴ˰���������plain��ʾtext����
# 3. �ʼ������ʽ

msg = MIMEText("Hello, i am beijing tulingxueyuan ", "plain", "utf-8")

# ����email��ַ���˴���ֱַ��ʹ���ҵ�qq��ż������һ����Ҫ��ʱ���룬�˴�͵��
from_addr = "1366798119@qq.com"
# �˴������Ǿ����������ú����Ȩ�룬���ǲ��ǲ������qq��������
from_pwd = "hjpovygcxmrshhcj"

# �ռ�����Ϣ
# �˴�ʹ��qq���䣬�Ҹ��Լ�����
to_addr = "1366798119@qq.com"


# ����SMTP��������ַ
# �˴����ݲ�ͬ���ʼ��������в�ͬ��ֵ��
# ���ڻ����κ�һ���ʼ������̣�������õ������շ��ʼ�������Ҫ������Ȩѡ��
# ��Ѷqq��������smtp��ַ�� smtp.qq.com

smtp_srv = "smtp.qq.com"

try:
    # ��������
    # ��һ���Ƿ�������ַ����һ����bytes��ʽ��������Ҫ����
    # �ڶ��������Ƿ������Ľ��ܷ��ʶ˿�
    srv = smtplib.SMTP_SSL(smtp_srv.encode(), 465) #SMTPЭ��Ĭ�϶˿�25
    #��¼���䷢��
    srv.login(from_addr, from_pwd)
    # �����ʼ�
    # ��������
    # 1. ���͵�ַ
    # 2. ���ܵ�ַ��������list��ʽ
    # 3. �������ݣ���Ϊ�ַ�������
    srv.sendmail(from_addr, [to_addr], msg.as_string())
    srv.quit()
except Exception as e:
    print(e)