#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 生成代码入口
import random

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
        test_method = methodObject(menthodNames[num - 1] + menthodNames[num][0].upper() + menthodNames[num][1:], needReturn, returnParam, params)
        arr.append(test_method)
        num += 1
    msg1 = '#import <Foundation/Foundation.h>'
    msg2 = '@interface ' + s + ' : NSObject'
    msg3 = '@end'
    text_createH(s, create_path, msg1, msg2, msg3, arr)

    #########
    msg5 = '#import <Foundation/Foundation.h>\n#import <CommonCrypto/CommonDigest.h>\n#import "' + s + '.h"'
    msg4 = '@interface ' + s + '()\n@end\n@implementation ' + s
    text_createM(s, create_path, msg5, msg4, msg3, arr)

