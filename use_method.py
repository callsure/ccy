#!/usr/bin/python
# -*- coding: UTF-8 -*-
# runshu.lin
import random
import shelve
import string

create_path = "/Users/xlin/Work/xcode/ccy/ccy"
full_path = create_path + '/use_db'
s = shelve.open(full_path)
rss = 'zyxwvutsrqponmlkjihgfedcba'
try:
    string_arrs = s['string_arrs']
    int_arr = s['int_arr']
    long_arr = s['long_arr']
    void_arr = s['void_arr']
    # print 'string类型返回------'
    # for arr in string_arrs:
    #     print arr.methodName
    # print 'int类型返回------'
    # for arr in int_arr:
    #     print arr.methodName
    # print 'long类型返回-----'
    # for arr in long_arr:
    #     print arr.methodName
    # print 'void类型返回-----'
    # for arr in void_arr:
    #     print arr.methodName
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