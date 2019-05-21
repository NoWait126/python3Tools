# -*- coding: utf-8 -*-

import sys, os, json
from testClass import Car

FUNCTION_FILE = "./built-in-functions.json"

FUNCTIONS      = {"abs": abs, "all": all, "any": any, "ascii": ascii, "bin": bin, "bool": bool, "callable": callable, "chr": chr, "@classmethod": print, "compile": compile, "complex":complex, "delattr": delattr, "dict":dict, "divmod": divmod, "enumerate":enumerate, "eval": eval, "exec": exec, "filter": filter, "float":float, "frozenset": frozenset, "getattr": getattr, "globals": globals, "hasattr": hasattr, "hash": hash, "hex": hex, "id": id, "input": input, "int": int, "isinstance": isinstance, "issubclass": issubclass, "iter": iter, "len": len, "list": list, "locals": locals, "map": map, "max": max, "min": min, "memoryview": memoryview, "next": next, "object":object, "oct": oct, "ord":ord, "pow": pow, "range": range, "repr": repr, "reversed": reversed, "round": round, "setattr": setattr, "sorted": sorted, "sum": sum, "type": type, "vars": vars, "zip": zip}


class FUNC(object):
    def __init__(self,name, funcDict):
        self.testFunc = FUNCTIONS[name]
        self.prototype = funcDict["prototype"]
        self.args = funcDict["args"]
        self.note = funcDict["note"]
        self.inputType = funcDict["input-type"]
        self.outputType = funcDict["output-type"]
        self.classArgs = Car()
    
         
    def printInput(self):
        print("-"*30)
        if self.inputType in ["n"]:
            print("入参说明 : {0}".format(self.args))
        elif self.inputType in ["", "object", "list", "str", "class", "char"]:
            print("入参说明 : {0}".format(self.args))
        elif self.inputType in ["iterable"]:
            print("入参说明 : {0}".format(list(self.args)))
        elif self.inputType in ["tuple"]:
            print("入参说明 : {0}".format(tuple(self.args)))
        elif self.inputType in ["bytes"]:
            print("入参说明 : bytes({0} {1})".format(self.args[0], self.args[1]))
    
    def getOutput(self):
        res = 0

        if self.outputType in [""]:
            return ""

        if self.inputType in ["tuple"]:
            res = self.testFunc(tuple(self.args))
        elif self.inputType in ["bytes"]:
            res = self.testFunc(bytes((self.args)[0], (self.args)[1]))
        elif self.inputType in ["iterable", "object", "str", "list", "char"]:
            res = self.testFunc(self.args)
        elif self.inputType in ["n"]:
            res = self.testFunc(* (self.args))
            
        elif self.inputType in ["class"]:
            self.classArgs.price = (self.args)["所有属性"]["price"]
            self.classArgs.speed = (self.args)["所有属性"]["speed"]
            self.classArgs.color = (self.args)["所有属性"]["color"]
            if "要操作的属性" in (self.args).keys():
                res = self.testFunc(self.classArgs, (self.args)["要操作的属性"])
            else:
                res = self.testFunc(self.classArgs)
        elif self.inputType in [""]:
            res = self.testFunc()
        #elif self.inputType == "iterable":
            
        return res

    def printOutput(self):
        print("-"*30)
        if self.outputType in ["", "num", "bool", "str", "char", "list", "tuple", "dict", "iterator", "range", "object", "None"]:
            print("函数出参 : {0}".format(self.getOutput()))
        elif self.outputType in ["iterable"]:
            print("函数出参 : {0}".format(list(self.getOutput())))
        elif self.outputType in ["class"]:
            classRes = self.getOutput()
            if None == classRes:
                print(("执行结果 : {0}".format(vars((self.classArgs)))))
            else:
                print(("执行结果 : {0}".format(classRes)))
        else:
            print("Unknow output type!")

    def funcExec(self):
        print("#"*30)
        print("函数原型 : {0}".format(self.prototype))
        self.printInput()
        self.printOutput()
        print("-"*30)
        print("函数作用 : {0}".format(self.note))
        print("-"*30)

def testFunc(funcName):
    f = open(FUNCTION_FILE, "r")
    funcMsg = json.load(f)
    funcDict = funcMsg[funcName]
    func = FUNC(funcName, funcDict)
    func.funcExec()

def testAll():
    for key in FUNCTIONS.keys():
        testFunc(key) 

def showAll():
    for key in FUNCTIONS.keys():
        print(key)

if  __name__ == '__main__':
    if len(sys.argv) < 2:
        print("enter a built-in function you want to test.")
        sys.exit(0)
    
    funcName = sys.argv[1]
    
    if "testAll" == funcName:
        testAll()
    
    elif "showAll" == funcName:
        showAll()
    
    elif "help" == funcName: 
        print("")
        print("showAll   --show all built-in funcitons.")
        print("testAll   --exec all built-in funcitons.")
        print("Function  --exec this built-in funciton,Function is a built-in function name.")
        print("")
    
    elif not funcName in FUNCTIONS:
        showAll()
        print("The function [{0}] is not supported, what we suppot now is above.".format(funcName))
        sys.exit(0)
    
    else:
        testFunc(funcName)


