# coding=gbk

import socket
'''
 - Client������
            1. ����ͨ�ŵ�socket
            2. �������ݵ�ָ��������
            3. ���ܷ����������ķ�������
'''

def clientFunc():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    text = "qweqweqwe"

    # ���͵����ݱ�ѧʽbytes��ʽ
    data = text.encode()

    # ����
    sock.sendto(data,("127.0.0.1", 5213))

    data,addr = sock.recvfrom(200)
    # �õ�����ֵ
    data = data.decode()

    print(data)

if __name__ == '__main__':
    clientFunc()
