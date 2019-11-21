#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 生成代码入口
import random
import shelve
import sys

from create_file import text_createH, text_createM
from create_method import classArray, methodObject
from random_word import load_word, random_word

s2 = sys.argv[1]
s1 = sys.argv[2]

create_path = "/Users/xlin/Work/xcode/ccy/ccy"
create_num = 3
if s1 != "":
    create_path = s1
if s2 != "":
    create_num = s2
load_word()
# 随机文件数量
ss = random_word(int(create_num))
#定义4个list存储
string_arrs = []
int_arr = []
long_arr = []
void_arr = []
for s in ss:
    arr = []
    menthodNum = random.randint(1, 4)
    menthodNames = random_word(menthodNum * 2)
    num = 1
    while num <= menthodNum:
        needReturn = False
        returnParam = ''
        i = random.randint(0, 1)
        if i == 1:
            needReturn = True
            returnParam = random.choice(classArray)

        params = []
        paramNum = random.randint(0, 3)
        if paramNum != 0:
            for i in range(paramNum):
                #随机参数
                pa = random.choice(classArray)
                params.append(pa)
        test_method = methodObject(menthodNames[num - 1] + menthodNames[num][0].upper() + menthodNames[num][1:], needReturn, returnParam, params, s)
        arr.append(test_method)
        num += 1
        if needReturn == True:
            if returnParam == 'int':
                int_arr.append(test_method)
            elif returnParam == 'NSString*':
                string_arrs.append(test_method)
            elif returnParam == 'long':
                long_arr.append(test_method)
        else:
            void_arr.append(test_method)
    msg1 = '#import <Foundation/Foundation.h>'
    msg2 = '@interface ' + s + ' : NSObject'
    msg3 = '@end'
    text_createH(s, create_path, msg1, msg2, msg3, arr)

    #########
    msg5 = '#import <Foundation/Foundation.h>\n#import <CommonCrypto/CommonDigest.h>\n#import "' + s + '.h"'
    msg4 = '@interface ' + s + '()\n@end\n@implementation ' + s
    text_createM(s, create_path, msg5, msg4, msg3, arr)

#########
#生成使用的文件
full_path = create_path + '/use_db'
s = shelve.open(full_path)
try:
    s['string_arrs'] = string_arrs
    s['int_arr'] = int_arr
    s['long_arr'] = long_arr
    s['void_arr'] = void_arr
finally:
    s.close()

