#!/usr/bin/python
# -*- coding: UTF-8 -*-
# runshu.lin
import random
import shelve
import string

import sys

create_path = "/Users/xlin/Work/xcode/ccy/ccy"
if len(sys.argv) > 1:
    create_num = sys.argv[1]

full_path = create_path + '/use_db'
s = shelve.open(full_path)
rss = 'zyxwvutsrqponmlkjihgfedcba'
try:
    string_arrs = s['string_arrs']
    int_arr = s['int_arr']
    long_arr = s['long_arr']
    void_arr = s['void_arr']

    # cppstring_arrs = s['cppstring_arrs']
    # cppint_arr = s['cppint_arr']
    # cpplong_arr = s['cpplong_arr']
    # cppvoid_arr = s['cppvoid_arr']
    # cppbool_arr = s['cppbool_arr']
finally:
    s.close()

def getStringReturn():
    if len(string_arrs):
        one = random.choice(string_arrs)
        s = '[' + one.fName + ' ' + one.methodName + addParamToCall(one.params, 0) + ']'
        return s
    else:
        return '@"' + randomString() + '"'
def getIntReturn():
    if len(int_arr):
        one = random.choice(int_arr)
        s = '[' + one.fName + ' ' + one.methodName + addParamToCall(one.params, 0) + ']'
        return s
    return random.randint(1, 1000)

def getLongReturn():
    if len(long_arr):
        one = random.choice(long_arr)
        s = '[' + one.fName + ' ' + one.methodName + addParamToCall(one.params, 0) + ']'
        return s
    return random.randint(1, 1000)

def getVoidReturn():
    if len(void_arr):
        one = random.choice(void_arr)
        s = '[' + one.fName + ' ' + one.methodName + addParamToCall(one.params, 0) + ']'
        return s
    return ''

#参数值，递归次数
def addParamToCall(params, times):
    ss = ''
    i = 0
    for param in params:
        if param == 'int' or param == 'long':
            p = random.randint(1, 1000)
            if i != 0:
                ss += ' param' + str(i) + ':' + str(p)
            else:
                ss += ':' + str(p)
        elif param == 'NSString*':
            p = randomString()
            if i != 0:
                ss += ' :@"' + p + '"'
            else:
                ss += ':@"' + p + '"'
        i += 1
    return ss

def randomString():
    return ''.join(random.sample(string.ascii_letters, 8))


###########获取cpp的方法调用########
# def getCppStringReturn():
#     if len(cppstring_arrs):
#         one = random.choice(cppstring_arrs)
#         s = one.fName + '::' + one.methodName + addParamToCallCpp(one.params, 0)
#         return s
#     return '"' + randomString() + '"'
# def getCppIntReturn():
#     if len(cppint_arr):
#         one = random.choice(cppint_arr)
#         s = one.fName + '::' + one.methodName + addParamToCallCpp(one.params, 0)
#         return s
#     return random.randint(1, 1000)
# def getCppLongReturn():
#     if len(cpplong_arr):
#         one = random.choice(cpplong_arr)
#         s = one.fName + '::' + one.methodName + addParamToCallCpp(one.params, 0)
#         return s
#     return random.randint(1, 1000)
# def getCppVoidReturn():
#     if len(cppvoid_arr):
#         one = random.choice(cppvoid_arr)
#         s = one.fName + '::' + one.methodName + addParamToCallCpp(one.params, 0)
#         return s
#     return ''
# def getCppBoolReturn():
#     if len(cppbool_arr):
#         one = random.choice(cppbool_arr)
#         s = one.fName + '::' + one.methodName + addParamToCallCpp(one.params, 0)
#         return s
#     return 'true'
#
# def addParamToCallCpp(params, times):
#     ss = '('
#     i = 0
#     for param in params:
#         if param == 'int' or param == 'long':
#             p = random.randint(1, 1000)
#             if i != 0:
#                 ss += ' ,' + str(p)
#             else:
#                 ss += str(p)
#         elif param == 'string':
#             p = randomString()
#             if i != 0:
#                 ss += ' ,"' + p + '"'
#             else:
#                 ss += '"' + p + '"'
#         elif param == 'bool':
#             j = random.randint(0, 1)
#             flag = 'true'
#             if j == 0:
#                 flag = 'false'
#             if i != 0:
#                 ss += ' ,' + flag
#             else:
#                 ss += flag
#         i += 1
#     ss += ')'
#     return ss