# -*- coding: utf-8 -*-



'''
高级语言通常都内置了一套try...except...finally...的错误处理机制

当某些代码可能会出错时，可以用try来运行这段代码,如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，即except语句块,执行完except后，如果有finally语句块，则执行finally语句块

'''

def div(s):
    return 10 / int(s)

if __name__ == '__main__':
    try:
        div(0)
    except Exception as e:
        print('Error:', e)
    except ZeroDivisionError as e:
        print('Never print this:', e)   # 由于前面捕获了Exception了异常，ZeroDivisionError是Exception的子，所以这个分钟永远都走不到
    finally:
        print('finally...')