# coding=gbk
from email.mime.text import MIMEText
from email.header import Header

msg = MIMEText("Hello wold",  "plain", "utf-8")
# ����������д��˵������ν�ķ����ߵĵ�ַ��ֻ�Ǵ�һ��Header�ĵ�һ��������Ϊ�ַ�������������
# ��utf8��������Ϊ�ܿ������ݰ�����Ӣ���ַ�
header_from = Header("��ͼ��ѧԺ���䷢��ȥ��<TuLingXueYuan@qq.cn>", "utf-8")
msg['From'] = header_from

# ��д��������Ϣ
header_to = Header("ȥ�������ĵط�<wangxiaojing@sina.com>", 'utf-8')
msg['To'] = header_to

header_sub = Header("����ͼ��ѧԺ������", 'utf-8')
msg['Subject'] = header_sub



# ���������ߵ�ַ�͵�¼��Ϣ
from_addr = "1366798119@qq.com"
from_pwd = "hjpovygcxmrshhcj"


# �����ʼ���������Ϣ
to_addr = "1366798119@qq.com"

smtp_srv = "smtp.qq.com"


try:
    import smtplib

    srv = smtplib.SMTP_SSL(smtp_srv.encode(), 465)

    srv.login(from_addr, from_pwd)
    srv.sendmail(from_addr, [to_addr], msg.as_string())
    srv.quit()

except Exception as e:
    print(e)