# coding=gbk
from email.mime.text import MIMEText #��������ʹ��
from email.mime.multipart import MIMEBase, MIMEMultipart # ���������ʼ�ʹ��


mail_mul = MIMEMultipart()
# �����ʼ�����
mail_text = MIMEText("Hello, i am liudana", "plain", "utf-8")
# �ѹ����õ��ʼ����ĸ������ʼ���
mail_mul.attach(mail_text)

# ��������
# ������������Ҫ�ӱ��ض��븽��
# ��һ�������ļ�
# ��rb��ʽ��
with open("02.html", "rb") as f:
    s = f.read()
    # ���ø�����MIME���ļ���
    m = MIMEText(s, 'base64', "utf-8")
    m["Content-Type"] = "application/octet-stream"
    # ��Ҫע�⣬
    # 1. attachment��ֺ�ΪӢ��״̬
    # 2. filename ������Ҫ�����Ű�����ע�����������Ŵ�
    m["Content-Disposition"] = "attachment; filename='02.html'"
    # ��ӵ�MIMEMultipart
    mail_mul.attach(m)



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
    import smtplib
    srv = smtplib.SMTP_SSL(smtp_srv.encode(), 465) #SMTPЭ��Ĭ�϶˿�25
    #��¼���䷢��
    srv.login(from_addr, from_pwd)
    # �����ʼ�
    # ��������
    # 1. ���͵�ַ
    # 2. ���ܵ�ַ��������list��ʽ
    # 3. �������ݣ���Ϊ�ַ�������
    srv.sendmail(from_addr, [to_addr], mail_mul.as_string())
    srv.quit()
except Exception as e:
    print(e)