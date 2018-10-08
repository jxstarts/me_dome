# coding=gbk
# ��Ҫ������Ӧ������Ҫ��ftplib
import ftplib # ����FTP�Ĳ���������������
import os
import socket

# �����־�ȷ��ʾ��ftp�������ϵ�ĳһ���ļ�
# �ö๫��ftp���������ʻ�������û�з�Ӧ
HOST = "ftp.acc.umu.se"
DIR = 'Public/EFLIB/'
FILE = 'README'

# 1. �ͻ�������Զ�������ϵ�FTP������
try:
    f = ftplib.FTP()
    # ͨ�����õ��Լ�����Է������
    f.set_debuglevel(2)
    # ����������ַ
    f.connect(HOST)
except Exception as e:
    print(e)
    exit()
print("***Connected to host {0}".format(HOST))



# 2. �ͻ��������û��������루���ߡ�anonymous���͵����ʼ���ַ��
try:
    # ��¼���û�������û���Ϣ����Ĭ��ʹ��������¼
    f.login()
except Exception as e:
    print(e)
    exit()
print("***Logged in as 'anonymous'")


# 3. �ͻ��˺ͷ��������и����ļ��������Ϣ��ѯ����
try:
    # ���ĵ�ǰĿ¼��ָ��Ŀ¼
    f.cwd(DIR)
except Exception as e:
    print(e)
    exit()
print("*** Changed dir to {0}".format(DIR))

try:
    # ��FTP�������������ļ�
    # ��һ��������ftp����
    # �ڶ��������ǻص�����
    # �˺�������˼�ǣ�ִ��RETR��������ļ������غ����лص�����
    f.retrbinary('RETR {0}'.format(FILE), open(FILE, 'wb').write)
except Exception as e:
    print(e)
    exit()

# 4. �ͻ��˴�Զ��FTP�������˳�����������
f.quit()