# -*- coding: utf-8 -*-

import socket, argparse, random

'''
一 关于socket库：该模块提供了访问BSD*套接字*的接口。适用于所有现代Unix系统、Windows、macOS等平台。任何系统的网络通信，背后都是围绕套接字来进行的。

二 关于本文件的代码：本文件的代码包含两对客户端服务器，即一对udp和一对tcp。

三 关键函数或者参数解析

  1 socket.socket(family=AF_INET, type=SOCK_STREAM, proto=0, fileno=None) 创建一个套接字

family：取值有AF_INET、AF_INET6、AF_UNIX，AF_INET是 IPv4 网络协议的套接字类型，AF_INET6 则是 IPv6 的；而 AF_UNIX 则是 Unix 系统本地通信。

type：取值有SOCK_STREAM和SOCK_DGRAM，SOCK_STREAM标识在IP层使用的是TCP协议即可靠的协议，SOCK_DGRAM标识使用的是UDP协议，即不可靠，使用UDP的话还有有一个特点就是支持广播，不过多播的出现已经让广播成为过时的技术

后面两个参数使用默认的即可

  bind((ip, port))           用于服务端，将socket绑定到某个IP的端口上面，也可以不绑定端口号，不绑定的话每次会随机分配一个端口号，ip为空的话表示系统会填写0.0.0.0，表示可以接收任意IP发来的数据
  
  getsockname()              返回给socket分配的IP和端口号

  connect(address)           连接到远程的socket，使用UDP的话可以不connect，但是connect是TCP客户端后续通信的首要步骤
  
  listen([backlog])          让TCP服务端开始接受连接请求， backlog代表最大的连接个数，默认为最大值，只有TCP服务端开始监听后，客户端才可以connect，在套节字上面运行该调用后会彻底改变套接字的角色，套接字只能监听连接请求，要调用accept函数创建新的socket与客户端通信
  
  accept()                   同意来自客户端的连接请求，返回两个参数：一个是新建的socket，这个socket用来和客户端通信；另外一个参数是tuple，表示客户端的ip和端口号
  
  getpeername()              获取客户端的地址
  
  send()                     向已经连接的socket发送数据，如果没有connect的话要使用sendto函数显示的标出目的地址，返回发送的字节数
  
  sendall(bytes[, flags])    向已经连接的socket发送数据，该函数和send不同，sendall会将所有的数据的都发送出去，而send是发送一次。sendall发送成功的话就返回None，不会返回发送的字节数，如果失败的话就会抛出异常

  sendto(bytes, (ip, port))  如果还没有connect连接的话，就需要使用sendto给出接收方的地址  

  recvfrom(bufsize[, flags]) 没有收到消息的时候它会循环等待，收到消息后会返回两个值(bytes, address)，一个是消息的内容一个是发送方的地址

  recv(bufsize[, flags])     返回接受到的数据，不会返回发送方的ip，收到数据后即使接收到的数据长度小于bufsize也会立即返回，如果没有及时调用该函数取走消息的话，数据量过大的时候可能会引起死锁
  
  shutdown(how)              用来关闭socket通信中的任一方向的连接，how的取值有socket.SHUT_WR表示不会再向套接字中读写数据，对方也不会去读；socket.SHUT_RD表示关闭接收方向的数据流，如果此时对方再发数据便会引发文件结束错误； socket.SHUTRDWR表示两个方向的都关闭
'''

def UDPServer(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((ip, port))

    print("listening at {}".format(sock.getsockname()))

    while True:
        data, address = sock.recvfrom(port)
        rand = random.random()
        print("random value", rand)
        if rand < 0.5:  # 模拟丢消息，不需要模拟丢消息可以去掉
            continue
        text = data.decode('ascii')
        print('The client at {} says {}'.format(address, text))
        text = "ha"
        data = text.encode('ascii')
        sock.sendto(data, address)


def UDPClient(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # sock.bind((ip, 65532))  # 不绑定的话会默认绑定到本地的一个随机端口
    sock.connect((ip, port))
    text = "hei"
    data = text.encode('ascii')
    while True:
        #sock.sendto(data, (ip, port))  # 已经connect的话不需要指定地址
        sock.send(data)
        print('Gotten from system address:{}'.format(sock.getsockname()))
        sock.settimeout(0.1)  # 设置0.1s的超时机制
        try:
            address = sock.recv(65535)
        except socket.timeout:
            raise RuntimeError("Did not get msg from server!")
        text = address.decode('ascii')
        print('The server sent me {}'.format(text))
        break # Test once


def TCPClient(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    print("Client has been assigned socket name ", sock.getsockname())
    sock.sendall(b'Hei')
    sock.shutdown(socket.SHUT_WR)
    print("has sent Hei")
    #reply = sock.recv(100)
    reply = recvAll(sock, 2)
    print("The server said ", repr(reply))
    sock.close()


def recvAll(sock, length):
    data = b''
    print("want lent:", length)
    while len(data) < length:
        more = sock.recv(length - len(data))
        if not more:
            raise EOFError("was expecting %d bytes but only recevied %d bytes before socket close" % (length, len(data)))
        data += more
    return data

def TCPServer(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((ip, port))
    sock.listen(1)
    print("Listening at ", sock.getsockname())
    while True:
        sc, sockname = sock.accept()
        print("Accepted a connection from ",sockname)
        print("  Socket name:", sc.getsockname())
        print("  Socket peer:", sc.getpeername())
        msg = recvAll(sc, 3)
        print("  Incoming message:", repr(msg))
        sc.sendall(b"Ha")
        sc.close()
        print("   reply sent, socket closed.")


if __name__ == '__main__':
    choices = {'UDPClient': UDPClient, 'UDPServer':UDPServer, 'TCPClient': TCPClient, 'TCPServer': TCPServer}
    parse = argparse.ArgumentParser(description='send and receive using UDP')
    parse.add_argument('role', choices=choices, help='which role to play')
    parse.add_argument('-p', metavar='PORT', type=int, default=65533, help='port')
    args = parse.parse_args()
    function = choices[args.role]
    function('127.0.0.1', args.p)



