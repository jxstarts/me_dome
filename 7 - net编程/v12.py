# coding=gbk
# ������ذ�
# poplib�����MDA��MUA����
import poplib

# ���°���������ʼ��ṹ����
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

# �õ��ʼ���ԭʼ����
# ���������Ҫ�����MDA��MUA�����ز�ʹ��Parse���Խ���
def getMsg():
    # ׼����Ӧ����Ϣ
    email = "1366798119@qq.com"
    # �������Ȩ��
    pwd = "hjpovygcxmrshhcj"

    # pop3��������ַ
    pop3_srv = "pop.qq.com" # �˿�995

    # ssl�����ǰ�ȫͨ��
    srv = poplib.POP3_SSL(pop3_srv)

    # user����email��ַ
    srv.user(email)
    # pass_��������
    srv.pass_(pwd)

    # ���²������ݾ���ҵ�����ʹ��
    # stat�����ʼ�������ռ�ÿռ�
    # ע��stat����һ��tuple��ʽ
    msgs, counts = srv.stat()
    print("Messages: {0}, Size: {1}".format(msgs, counts))

    # list���������ʼ�����б�
    # mails�������ʼ�����б�
    rsp, mails, octets = srv.list()
    # ���Բ鿴���ص�mails�б�����[b'1 82923', b'2 2184', ...]
    print(mails)


    # ��ȡ����һ���ʼ���ע�⣬�ʼ��������Ǵ�1��ʼ, ���´������������
    index = len(mails)
    # retr���𷵻�һ�����������ŵ�һ���ŵ����ݣ������ݲ����пɶ���
    # lines �洢�ʼ�����ԭʼ�ı���ÿһ��
    rsp, lines, octets = srv.retr(index)

    # ��������ʼ���ԭʼ�ı�
    msg_count = b'\r\n'.join(lines).decode("utf-8")
    # �������ʼ������ṹ��
    # �����ǽ������ʼ�����
    msg = Parser().parsestr(msg_count)

    #�ر�����
    srv.quit()

    return msg


# ��ϸ�����õ����ʼ�����
# msg�������ʼ���ԭʼ����
# idnent��������ʼ�Ƕ�׵Ĳ㼶
def parseMsg(msg, indent=0):
    '''
    1. �ʼ���ȫ��������Ƕ�׸�ʽ
    2. �ʼ�ֻ��һ��From��To��Subject֮�����Ϣ

    :param msg:
    :param indent: �����ʼ������м����ʼ�MIMEXXX���͵�����,չʾ��ʱ�������Ӧ����
    :return:
    '''

    # ��취��ȡ��ͷ����Ϣ
    # ֻ���ڵ�һ����ʼ��вŻ���������ݣ�
    # ������ֻ��һ��
    if indent == 0:
        for header in ['From', "To", 'Subject']:
            # ʹ��get���Ա������û����عؼ��ֱ���Ŀ�����
            # ���û�� �ؼ��֡�From���� ����ʹ�� msg["From"]�ᱨ��
            value = msg.get(header, '')
            if value:
                # Subject�е�����ֱ�ӽ���Ϳ��ԣ������ַ�������
                if header == 'Subject':
                    value = decodeStr(value)
                # �����From��To�ֶΣ������ݴ���� "�ҵ�����<xxxxx@qq.com>�����ָ�ʽ
                else:
                    hdr, addr = parseaddr(value)
                    name = decodeStr(hdr)
                    # ���շ�������  "�ҵ�����<xxx@qq.com>�ĸ�ʽ
                    value = "{0}<{1}>".format(name, addr)
            print("{0}, {1}: {2}".format(indent, header, value))

    # ��������ע�ʼ����ݱ���
    # �ʼ������У��п�����multipart���ͣ�Ҳ�п�������ͨ�ʼ�����
    # ����Ľ���ʹ�õݹ鷽ʽ
    if (msg.is_multipart()):
        # �����multipart���ͣ�����õݹ����

        # �õ��ಿ���ʼ���һ�������ʼ�����
        parts = msg.get_payload()
        # enumerate ���������ú���
        # �����ǽ�һ���б��˴���parts������һ����������partsԭ���ݹ��ɵ��µ��б�
        # ���� enumerate(['a', 'b', 'c']) �����:  [(1,'a'), (2, 'b'), (3, 'c')]
        for n,part in enumerate(parts):
            # һ���ַ�������һ�����ֵ���˼�Ƕ�����ַ�������n����չ
            # ���� ��aa" * 2 -> "aaaa"
            print("{0}spart: {1}".format(' '*indent, n))
            parseMsg(part, indent+1)
    else: # ��������
        # get_content_type��ϵͳ�ṩ�������õ���������
        content_type = msg.get_content_type()
        # text/plain ���� text/html�ǹ̶�ֵ
        if content_type == 'text/plain' or content_type == 'text/html':
            content = msg.get_payload(decode=True)
            charset = guessCharset(msg)
            if charset:
                content = content.decode(charset)
            print("{0}Text: {1}".format(indent, content))

        else: #�����ı����ݣ���Ӧ���Ǹ���
            print('{0}Attachment: {1}'.format(indent, content_type))

def decodeStr(s):
    '''
    s����һ���ʼ���From��To��Subject�е���һ��
    ��s���н��룬�����Ǳ���������
    :param s:
    :return:
    '''
    value, charset = decode_header(s)[0]
    # charset��ȫ����Ϊ��
    if charset:
        # ���ָ�����룬����ָ�������ʽ���н���
        value = value.decode(charset)

    return value

def guessCharset(msg):
    '''
    �²��ʼ��ı����ʽ
    :param msg:
    :return:
    '''
    # �����ֳɵĺ���
    charset = msg.get_charset()

    if charset is None:
        # �ҵ��������ͣ���ת����Сд
        content_type = msg.get("Content-Type", "").lower()
        pos = content_type.find("charset=")
        if pos >= 0:
            # �������chraset������������ charset=xxxx
            charset = content_type[pos+8:].strip()

    return  charset




if __name__ == "__main__":
    # �õ��ʼ���ԭʼ����
    msg = getMsg()
    print(msg)
    # ��ȷ�����ʼ�����
    parseMsg(msg, 0)
