


'''
select监视的文件有三类：writefds、readfds、exceptfds

调用select后会阻塞，知道有描述符就绪

select单个进程最多监视1024个描述符

poll使用pollfd指针，包含要监视的event和要发生的event

poll无最大的限制

epoll是select和poll的增强版，查找使用红黑树，无Windows的支持


'''