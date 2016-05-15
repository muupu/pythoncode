import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #SOCK_DGRAM - Socket的类型是UDP
# 绑定端口:
s.bind(('127.0.0.1', 9999))

# UDP不需要调用listen()方法，而是直接接收来自任何客户端的数据

print('Bind UDP on 9999...')
while True:
    # 接收数据:
    data, addr = s.recvfrom(1024)  #返回数据和客户端的地址与端口
    print('Received from %s:%s.' % addr) # addr包含客户端的地址与端口，是个tuple
    s.sendto(b'Hello, %s!' % data, addr) #服务器收到数据后，直接调用sendto()就可以把数据用UDP发给客户端。不需要多线程。

s.close()