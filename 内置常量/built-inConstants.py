# -*- coding: utf-8 -*-

import sys, os, json

const = {
    "False" :  "bool 类型的假值。 给 False 赋值是非法的并会引发 SyntaxError。",
    "True"  : "bool 类型的真值。 给True 赋值是非法的并会引发 SyntaxError。",
    "None"  : "NoneType 类型的唯一值，None 经常用于表示缺少值，当因为默认参数未传递给函数时，给None赋值是非法的并会引发 SyntaxError。"
}

if  __name__ == '__main__':
    print("#"*30)
    for i in const.keys():
        print("{0}: {1}".format(i, const[i]))
        print("-"*30)
