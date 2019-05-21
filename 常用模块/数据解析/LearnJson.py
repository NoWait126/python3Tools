# -*- coding: utf-8 -*-

import json

'''
json数据以键值对方式存储，方便解析，比xml用处更广

1 json.dumps()   将obj序列化为 JSON 格式的str

2 json.dump()    使用这个 conversion table 来序列化 obj 为一个JSON格式的流到一个文件上面

  dumps和dump名字相近但是功能完全不同

3 json.load(fp)  将fp反序列化为一个Python对象

4 josn.loads()   和dumps是对函数，loads是将str转为dict

'''

jsonData = {"one": "1", "two": "2", "three": "3"}

def testFunc():
    dumpsMonths = json.dumps(jsonData)
    loadsMonths = json.loads(dumpsMonths)
    print("未经过dumps转换的数据格式：", type(jsonData))
    print("经过dumps函数转换的数据格式：%s, 内容为：%s" % (type(dumpsMonths), dumpsMonths))
    print("经过loads函数转换的数据格式：%s, 内容为：%s\n" % (type(loadsMonths), loadsMonths))

    print("使用dump，将数据写入del.txt文件")
    fp = open("del.txt", 'w')
    json.dump(jsonData, fp)
    fp.close()

def analyJson(jsonfile):
    print("\n解析json文件%s:\n" % jsonfile)
    f = open(jsonfile, "r")
    bookMsg = json.load(f)
    books = bookMsg.keys()
    for book in books:
        print("boos:", book)
        print(bookMsg[book]["type"])
        print(bookMsg[book]["price"])
        print(bookMsg[book]["year"])
        print("\n")

if __name__ == '__main__':
    testFunc()
    analyJson("book.json")