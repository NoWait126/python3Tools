一 概述

1 环境要求

  python3，如果不想影响其他Python工程的开发，可以使用virtualenv安装独立的环境，virtualenv使用见`Python开发工具.txt`

2 项目说明

  这是一个学习Python3标准库的工程，包括Python3的内置函数、常用的标准库、Python开发的一些开发辅助工具、Python一些特有功能。

  项目知识点是自己学习的时候结合官方文档、书籍、网络资料总结而成，仅供学习交流使用。

3 编程规范  

  项目中模块的函数有些是嵌套写法，这种写法不是一个好的编程风格，完全是为了统一风格和模块相互之间保持独立。

二 各个文件夹说明

1 内置函数
 
  该文件夹下是所有Python3的内置函数，执行的时候后面加上想要测试的函数即可。参数和函数说明在built-in-functions.json文件中。除了个别的不能实现外，其他函数执行的过程并不是只是将json文件中的参数输出，而是确实在环境上面执行了输入的函数。输入showAll可以查看所有的内置函数，输入testAll可以执行全部的内置函数。

  示例：Python built-in-functions.py add      即可在当前环境下执行add函数
  
       Python built-in-functions.py showAll  显示所有支持的内置函数
       
       Python built-in-functions.py testAll  执行所有支持的内置函数
  
  展望：目前内置函数仅仅支持固定好的参数，1 后期将支持用户输入参数；2 用户可以将此文件夹打包为Python可执行文件放在本地，开发时如有需要可以随时执行，方便查看学习
  
2 内置常量

  Python的常用的内置常量
  
3 常用模块
  
  下面包括的文件夹以及各个文件夹里面使用的库, 任何文件夹下的py文件都是可以执行的文件
  
  互联网协议支持：使用ftplib、paramiko、urllib等完成文件上传、发送远端命令、解析网络页面
  
  加密服务     ：使用hashlib对字符串进行加密
  
  并发执行     ：使用threading、multiprocess、Queue等进行多线程和多进程的操作，
               后续增加select、asyncio等库实现异步io和协程的操作
  
  数据解析     ：使用Json、xml的sax和dom方式对json和xml数据进行解析
  
  文件和目录访问：使用os.path和pathlib进行目录访问
  
  网络通信     ：使用select库进行网络编程，实现了TCP和UDP两中服务器和客户端的连接   
  
  调试程序     ：使用Pdb进行程序调试
  
 4 附加功能
   介绍Python的Decorator、lambda、和yield用法，即装饰器、匿名函数和生成器
