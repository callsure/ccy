#!/usr/bin/python
# -*- coding: UTF-8 -*-
# runshu.lin
import random
import shelve
import sys

from create_file import text_createHpp, text_createCpp
from create_method import methodObject
from random_word import random_word

####这里的代码最好跟生成的oc代码目录分开，防止重名文件
create_path = "/Users/xlin/Work/xcode/ccy/ccy/gg"
create_num = 10
if len(sys.argv) > 2:
    create_num = sys.argv[1]
    create_path = sys.argv[2]
elif len(sys.argv) == 2:
    create_num = sys.argv[1]

cppArray = ['string', 'int', 'long', 'bool']
# 随机文件数量
ss = random_word(int(create_num))
#定义4个list存储
string_arrs = []
int_arr = []
long_arr = []
void_arr = []
bool_arr = []
for sa in ss:
    s = sa[0].upper() + sa[1:]
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
            returnParam = random.choice(cppArray)
        params = []
        paramNum = random.randint(0, 3)
        if paramNum != 0:
            for i in range(paramNum):
                #随机参数
                pa = random.choice(cppArray)
                params.append(pa)
        test_method = methodObject(menthodNames[num - 1] + menthodNames[num][0].upper() + menthodNames[num][1:], needReturn, returnParam, params, s)
        arr.append(test_method)
        num += 1
        if needReturn == True:
            if returnParam == 'int':
                int_arr.append(test_method)
            elif returnParam == 'string':
                string_arrs.append(test_method)
            elif returnParam == 'long':
                long_arr.append(test_method)
            elif returnParam == 'bool':
                bool_arr.append(test_method)
        else:
            void_arr.append(test_method)
    f_name = s + '_hpp'
    msg1 = '#ifndef ' + f_name + '\n#define ' + f_name + '\n#include <string>\nusing namespace std;\n'
    msg2 = 'class ' + s + '\n{'
    msg3 = '};\n#endif\n'
    text_createHpp(s, create_path, msg1, msg2, msg3, arr)

    #########
    msg5 = '#include "' + s + '.hpp"\n#include <string>\n#include <iostream>\n#include <cmath>\n#include "LaData.h"\nusing namespace std;\n'
    msg4 = ''
    text_createCpp(s, create_path, msg5, msg4, msg3, arr)

#生成使用的文件
full_path = create_path + '/use_db'
s = shelve.open(full_path)
try:
    s['cppstring_arrs'] = string_arrs
    s['cppint_arr'] = int_arr
    s['cpplong_arr'] = long_arr
    s['cppvoid_arr'] = void_arr
    s['cppbool_arr'] = bool_arr
finally:
    s.close()
