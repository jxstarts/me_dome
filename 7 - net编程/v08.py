# coding=gbk
from email.mime.text import  MIMEText

mail_content = """
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

msg = MIMEText(mail_content, "html", "utf-8")

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