#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random

#生成oc的.h文件
from create_method import handle_method


def text_createH(fileName, path, msg1, msg2, msg3, methodArray):
    full_path = path + '/' + fileName + '.h'
    file = open(full_path, "w+")
    #文件头注释
    notes = '//\n//' + fileName + '.h\n//\n//Created by runshu.lin\n'
    file.truncate()
    file.write(notes)
    file.write(msg1 + '\n')
    file.write(msg2 + '\n')
    for method in methodArray:
        methodHead = ''
        if method.needRetuen:
            #这里先写死，返回类型应该随机
            methodHead = method.returnType
        else:
            methodHead = 'void'
        methodPamam = ''
        i = 0
        for pa in method.params:
            if pa == 'NSString*':
                methodPamam += ':(' + pa +')param' + str(i) + ' '
            else:
                if i == 0:
                    methodPamam += ':(' + pa + ')param' + str(i) + ' '
                else:
                    methodPamam += 'param' + str(i) + ':' + '(' + pa + ')param' + str(i) + ' '
            i += 1
        methodPamam = methodPamam.rstrip()
        if methodPamam == '':
            file.write('+(' + methodHead + ') ' + method.methodName + ';\n')
        else:
            file.write('+(' + methodHead + ') ' + method.methodName + methodPamam + ';\n')
    file.write('\n')
    file.write(msg3)
    file.flush()
    file.close()

#生成oc的.m文件
def text_createM(fileName, path, msg1, msg2, msg3, methodArray):
    full_path = path + '/' + fileName + '.m'
    file = open(full_path, "w+")
    #文件头注释
    notes = '//\n//' + fileName + '.h\n//\n//Created by runshu.lin\n'
    file.truncate()
    file.write(notes)
    file.write(msg1 + '\n')
    file.write(msg2 + '\n')
    for method in methodArray:
        methodHead = ''
        if method.needRetuen:
            #这里先写死，返回类型应该随机
            methodHead = method.returnType
        else:
            methodHead = 'void'
        methodPamam = ''
        i = 0
        for pa in method.params:
            if pa == 'NSString*':
                methodPamam += ':(' + pa +')param' + str(i) + ' '
            else:
                if i == 0:
                    methodPamam += ':(' + pa + ')param' + str(i) + ' '
                else:
                    methodPamam += 'param' + str(i) + ':' + '(' + pa + ')param' + str(i) + ' '
            i += 1
        methodPamam = methodPamam.rstrip() + ' {\n'
        if methodPamam == '':
            file.write('+(' + methodHead + ') ' + method.methodName)
        else:
            file.write('+(' + methodHead + ') ' + method.methodName + methodPamam)

        methodBody = handle_method(method.returnType, method.params)
        file.write(methodBody)
        file.write('}\n')

    file.write('\n')
    file.write(msg3)
    file.flush()
    file.close()