# -*- coding :utf-8 -*-

import xml.sax
from xml.dom.minidom import parse

'''
操作XML有两种方法：DOM和SAX

一 DOM：把整个XML读入内存，解析为树，占用内存大，解析慢，但是可以任意遍历树的节点

二 SAX：流模式，边读边解析，占用内存小，解析快，但是我们需要自己处理事件

  startElement()                                # 内容开始事件

  characters()                                  # 内容事件

  endElement()                                  # 内容结束事件

  1 xml.sax.make_parser( [parser_list] )　　     # 创建一个新的解析器对象并返回
  
  2 XMLReader.setFeature(featurename, value)    # 为value设置特征名，特征名是未识别的话抛出SAXNotRecognizedException异常
  
  3 XMLReader.getFeature(featurename)           # 返回当前设置的特征名，特征名是未识别的话抛出SAXNotRecognizedException异常

  4 XMLReader.getProperty(propertyname)         # 返回当前属性名的设置

  5 XMLReader.setProperty(propertyname, value)  # 为value设置属性名
'''

class BooksHandel(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.type = ""
        self.name = ""
        self.price = ""
        self.year = ""

    def startElement(self, tag, attr):
        self.CurrentData = tag
        if "book" == tag:
            print("\nbook:")
            self.name = attr["title"]
            print("name:", self.name)

    def endElement(self, tag):
        if self.CurrentData == "type":
            print("type:", self.type)
        elif self.CurrentData == "year":
            print("year:", self.year)
        elif self.CurrentData == "price":
            print("price:", self.price)

        self.CurrentData = ""

    def characters(self, content):
        if self.CurrentData == "type":
            self.type = content
        elif self.CurrentData == "year":
            self.year = content
        elif self.CurrentData == "price":
            self.price = content

def analyUseSax():
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    Handler = BooksHandel()
    parser.setContentHandler(Handler)
    parser.parse('book.xml')


# 使用dom解析
def analyUseDom():
    domTree = xml.dom.minidom.parse("book.xml")
    coll = domTree.documentElement
    books = coll.getElementsByTagName("book")
    for book in books:
        print("book:")
        if book.hasAttribute("title"):
            print("Title: %s" % book.getAttribute("title"))

        type = book.getElementsByTagName('type')[0]    # [0]：若存在同名的，用以区分
        price = book.getElementsByTagName('price')[0]    # [0]：若存在同名的，用以区分
        year = book.getElementsByTagName('year')[0]    # [0]：若存在同名的，用以区分
        print("Type: %s" % type.childNodes[0].data)    # type.childNodes[0]表示type标签下的第一个内容或者子标签
        print("price: %s" % price.childNodes[0].data)    # type.childNodes[0]表示type标签下的第一个内容或者子标签
        print("year: %s" % year.childNodes[0].data)    # type.childNodes[0]表示type标签下的第一个内容或者子标签


if __name__ == '__main__':
    print("使用sax解析：")
    analyUseSax()

    print("\n使用dom解析：")
    analyUseDom()


