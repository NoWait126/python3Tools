# -*- coding: utf-8 -*-

import argparse, paramiko, sys, threading, functools


'''
paramiko：遵循SSH2协议，支持以加密和认证的方式，用于远程服务器的连接

paramiko安装方式pip install -e git+https://github.com/paramiko/paramiko/#egg=paramiko

本文件两个示例
  exComm 是使用该库连接本机，然后输入命令
  
  downloadFile 是下载远端主机的文件
'''

class AllowAnythingPolicy(paramiko.MissingHostKeyPolicy):
    def missing_host_key(self, client, hostname, key):
        return

def readRet(fileobj):
    s = fileobj.readline()
    while s:
        print(s.strip())
        s = fileobj.readline()

def exComm(hostname, username, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(AllowAnythingPolicy())
    client.connect(hostname, username=username, password=password)

    ret1 = client.exec_command('pwd')
    ret2 = client.exec_command('mkdir testDir')
    thread1 = threading.Thread(target = readRet, args=(ret1[1],))
    thread2 = threading.Thread(target = readRet, args=(ret2[1],))

    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

    client.close()

def transStatus(filename, byte_so_far, bytes_total):
    percent = 100. * byte_so_far / bytes_total
    print('Transporting %s, %.1f' % (filename, percent))

def downloadFile(hostname, username, password, filename):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(AllowAnythingPolicy())
    client.connect(hostname, username=username, password=password)
    sftp = client.open_sftp()

    callback = functools.partial(transStatus, filename)
    sftp.get(filename, filename + '.copy', callback=callback)

    client.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='tranport file throw ssh')
    parser.add_argument('hostname', help='target ip')
    parser.add_argument('username', help='username of target ip')
    parser.add_argument('password', help='password for username')
    parser.add_argument('file', default="", help='file name')
    args = parser.parse_args()
    if "" != args.file:
        downloadFile(args.hostname, args.usename, args.password, args.file)
    else:
        exComm(args.address, args.username, args.password)