# coding=gbk
import socket

def tcp_srv():
    # 1. ����socket�������ͨ�ţ����socket��ʵֻ������ܶԷ�����������ͨ�ŵ������Ӻ���½�����socket
    # ��Ҫ�õ���������
    # AF_INET: ����ͬudpһ��
    # SOCK_STREAM: ������ʹ�õ�tcp����ͨ��
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2. �󶨶˿ں͵�ַ
    # �˵�ַ��Ϣ��һ��Ԫ���������ݣ�Ԫ��������֣���һ����Ϊ�ַ���������ip���ڶ�����Ϊ�˿ڣ���һ���������Ƽ�����10000
    addr = ("127.0.0.1", 8998)
    sock.bind(addr)
    # 3. ��������ķ���socket
    sock.listen()
    # print(sock.accept())
    while True:
        # 4. ���ܷ��ʵ�socket�����������ܷ��ʼ�������һ��ͨѶ������ͨ·
        # accept���ص�Ԫ���һ��Ԫ�ظ�ֵ��skt���ڶ�����ֵ��addr
        skt, addr = sock.accept()
        # 5. ���ܶԷ��ķ������ݣ����ý��յ���socket��������
        # 500�������ʹ�õ�buffersize
        # msg = skt.receive(500)
        msg = skt.recv(500)
        # ���ܵ�����bytes��ʽ����
        # ��õ�str��ʽ�ģ���Ҫ���н���
        msg = msg.decode()

        rst = "Received msg: {0} from {1}".format(msg, addr)

        # print(sock.accept())
        print(rst)
        # 6. ����б�Ҫ�����Է����ͷ�����Ϣ
        skt.send(rst.encode())

        # 7. �ر�����ͨ·
        skt.close()

if __name__ == "__main__":
    print("Starting tcp server.......")
    tcp_srv()
    print("Ending tcp server.......")