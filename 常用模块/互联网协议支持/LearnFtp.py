# -*- coding: utf-8 -*-

from ftplib import FTP
import sys, getpass, os.path, argparse

'''
本示例是使用ftplib上传二进制文件

需要注意的是目标主机需要安装ftp服务，并修改vsftpd.conf文件（默认在/etc/vsftpd.conf），将write_enable=YES，并重启sftp服务sudo service vsftpd restart

'''

def uploadFile(hostname, username, oriFile):
    password = getpass.getpass("enter password")

    ftp = FTP(hostname)
    ftp.login(username, password)
    ftp.cwd("/home/think/testDir") # 找到远端工作目录
    with open(oriFile, 'rb') as f:
        ftp.storbinary('STOR %s' % os.path.basename(oriFile), f)
    ftp.quit()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='tranport file throw ssh')
    parser.add_argument('hostname', help='target ip')
    parser.add_argument('username', help='username of target ip')
    parser.add_argument('oriFile', default="", help='origin file name')
    args = parser.parse_args()
    uploadFile(args.hostname, args.usename, args.oriFile)
