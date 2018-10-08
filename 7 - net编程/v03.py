# coding=gbk

'''
  - Server������
            1. ����socket��socket�Ǹ������ͨ�ŵ�һ��ʵ��
            2. �󶨣�Ϊ������socketָ�ɹ̶��Ķ˿ں�ip��ַ
            3. ���ܶԷ���������
            4. ���Է����ͷ������˲���Ϊ�Ǳ��벽��
'''

# socketģ�鸺��socket���
import socket
# ģ��������ĺ���
def serverFunc():
    # 1.����socket

    # socket.AF_INET :ʹ��ipv4Э����
    # socket.SOCK_DGRAM: ʹ��UDPͨ��
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2.��IP����port
    # 127.0.0.1: ���IP��ַ������ǻ�������
    # 5213������ָ���Ķ˿ں�
    # ��ַ��һ��tuple���ͣ���IP�� port��
    addr = ("127.0.0.1", 5213)
    sock.bind(addr)

    # 3. ���ܶԷ���Ϣ
    # �ȴ���ʽΪ���� ��û������������
    # recvfrom���ܵķ���ֵ��һ��Ԫ��tuple�� Ǯ�����ʾ���ݣ���һ���ʾ��ַ
    # �����ĺ����ǻ�������С
    # rst = sock.recvfrom(500)
    data,addr = sock.recvfrom(500)

    print(data)

    print(type(data))

    # ���͹�����������bytes��ʽ������ͨ��������ܵõ�str��ʽ����
    #decodeĬ�ϲ�����utf-8
    text = data.decode()
    print(type(text))
    print(text)

    # 4.���Է����ص���Ϣ
    rsp = "hahahahahahah"

    # ���͵�������Ҫ�����bytes��ʽ
    # Ĭ����utf8
    data = rsp.encode()

    sock.sendto(data, addr)

if __name__ == '__main__':
    import time
    print("start server.........")
    while True:
        try:
            serverFunc()
        except Exception as e:
            print(e)
        time.sleep(1)
    print("ending server...........")
