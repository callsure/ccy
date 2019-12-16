#!/usr/bin/python
# -*- coding: UTF-8 -*-
# runshu.lin
# 转换基本类型
import random

#bool -> int
def transCpp_Bool_Int(index, param):
    res = 'time_t now_' + str(index + 1) + ' = time(0);\n'
    res += 'int cc_' + str(index) + ' = 0;\n'
    res += 'if (' + param + ')\n'
    res += 'cc_' + str(index) + ' = (int) now_' + str(index + 1) + ' % ' + str(random.randint(222222, 666666)) + ';\n'
    res += 'else\n'
    res += 'cc_' + str(index) + ' = (int) now_' + str(index + 1) + ' % ' + str(random.randint(222222, 666666)) + ';\n'
    return res

#bool -> long
def transCpp_Bool_Long(index, param):
    res = 'time_t now_' + str(index + 1) + ' = time(0);\n'
    res += 'long cc_' + str(index) + ' = 0;\n'
    res += 'if (' + param + ')\n'
    res += 'cc_' + str(index) + ' = now_' + str(index + 1) + ' % ' + str(random.randint(222222, 666666)) + ';\n'
    res += 'else\n'
    res += 'cc_' + str(index) + ' = now_' + str(index + 1) + ' % ' + str(random.randint(222222, 666666)) + ';\n'
    return res

#bool -> string
def transCpp_Bool_String(index, param):
    res = 'time_t now_' + str(index + 1) + ' = time(0);\n'
    res += 'string cc_' + str(index) + ';\n'
    res += 'if (' + param + ')\n'
    res += 'cc_' + str(index) + ' = to_string(now_' + str(index + 1) + ' % ' + str(random.randint(222222, 666666)) + ');\n'
    res += 'else\n'
    res += 'cc_' + str(index) + ' = to_string(now_' + str(index + 1) + ' % ' + str(random.randint(222222, 666666)) + ');\n'
    return res

#int -> bool
def transCpp_Int_Bool(index, param):
    res = 'int dd_' + str(index + 1) + ' = ' + param + ';\n'
    res += 'bool cc_' + str(index) + ' = dd_' + str(index + 1) + ' % 20 == 0 ? true : false;\n'
    return res

#int -> Long
def transCpp_Int_Long(index, param):
    res = 'int dd_' + str(index + 1) + ' = ' + param + ';\n'
    res += 'long cc_' + str(index) + ' = dd_' + str(index + 1) + ' * ' + str(random.randint(10, 20)) + ';\n'
    return res

#int -> String
def transCpp_Int_String(index, param):
    res = 'int dd_' + str(index + 1) + ' = ' + param + ';\n'
    res += 'string cc_' + str(index) + ' = to_string(dd_' + str(index + 1) + ' / ' + str(random.randint(10, 20)) + ');\n'
    return res

#long -> bool
def transCpp_Long_Bool(index, param):
    res = 'long dd_' + str(index + 1) + ' = ' + param + ';\n'
    res += 'bool cc_' + str(index) + ' = dd_' + str(index + 1) + ' % 20 == 0 ? true : false;\n'
    return res

#long -> int
def transCpp_Long_Int(index, param):
    res = 'long dd_' + str(index + 1) + ' = ' + param + ';\n'
    res += 'int cc_' + str(index) + ' = (int) dd_' + str(index + 1) + ' / ' + str(random.randint(1000, 2000)) + ';\n'
    return res

#long -> String
def transCpp_Long_String(index, param):
    res = 'long dd_' + str(index + 1) + ' = ' + param + ';\n'
    res += 'string cc_' + str(index) + ' = to_string(dd_' + str(index + 1) + ' / ' + str(random.randint(10, 20)) + ');\n'
    return res

#string -> bool
def transCpp_String_Bool(index, param):
    res = 'string dd_' + str(index + 1) + ' = ' + param + ';\n'
    res += 'bool cc_' + str(index) + ' = dd_' + str(index + 1) + '.length() % 20 == 0 ? true : false;\n'
    return res

#string -> int
def transCpp_String_Int(index, param):
    res = 'string dd_' + str(index + 1) + ' = ' + param + ';\n'
    res += 'int cc_' + str(index) + ' = dd_' + str(index + 1) + '.length() * ' + str(random.randint(10, 50)) + ';\n'
    return res

#long -> String
def transCpp_String_Long(index, param):
    res = 'string dd_' + str(index + 1) + ' = ' + param + ';\n'
    res += 'long cc_' + str(index) + ' = dd_' + str(index + 1) + '.length() * ' + str(random.randint(10, 50)) + ';\n'
    return res