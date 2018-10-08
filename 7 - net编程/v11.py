# coding=gbk
from email.mime.text import  MIMEText
from email.mime.multipart import  MIMEMultipart

# ����һ��MIMEMultipart�ʼ�
msg = MIMEMultipart("alternative")

# ����һ��HTML�ʼ�����
html_content = """
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>Title</title>
            </head>
            <body>

            <h1> ����һ��HTML��ʽ�ʼ�</h1>

            </body>
            </html>
        """
#
msg_html = MIMEText(html_content, "html", "utf-8")
msg.attach(msg_html)


msg_text = MIMEText("just text content", "plain", "utf-8")
msg.attach(msg_text)



# ����email��ַ���˴���ֱַ��ʹ���ҵ�qq���䣬������ʱ����
from_addr = "1366798119@qq.com"
#from_pwd = input('163��������: ')
from_pwd = "hjpovygcxmrshhcj"

# �ռ�����Ϣ:
# �˴�ʹ����ע���163����
to_addr = "1366798119@qq.com"

# ����SMTP��������ַ:
# �˵�ַ����ÿ���ʼ��������в�ͬ��ֵ,����Ƿ����ʼ������̵�smtp��ַ
# ���õ���qq���䷢�ͣ��˴�Ӧ����д��Ѷqq�����smtpֵ,��smtp.163.com,
# ��Ҫ������Ȩ�룬
smtp_srv = "smtp.qq.com"

try:
    import smtplib
    # ���ܴ���
    #server = smtplib.SMTP_SSL(smtp_srv.encode(), 465) # SMTPЭ��Ĭ�϶˿���25
    # qq����Ҫ��ʹ�� TLS���ܴ���
    server = smtplib.SMTP(smtp_srv.encode(), 25) # SMTPЭ��Ĭ�϶˿���25
    server.starttls()
    # ���õ��Լ���
    # ͨ�����õ��Եȼ�����������Ŀ��������ʼ��Ľ�������
    server.set_debuglevel(1)
    # ��¼��������
    server.login(from_addr, from_pwd)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()
except Exception as e:
    print(e)


