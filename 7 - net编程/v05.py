# coding=gbk
import socket

def tcp_clt():
    # 1. ����ͨ��socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2. ���ӶԷ���������Է�����ͨ·
    addr = ("127.0.0.1", 8998)
    sock.connect(addr)
    # 3. �������ݵ��Է�������
    msg = "I love wangxiaojing"
    sock.send(msg.encode())
    # 4. ���ܶԷ��ķ���
    rst = sock.recv(500)
    print(rst.decode())
    # 5. �ر�����ͨ·
    sock.close()


if __name__ == "__main__":
    tcp_clt()
