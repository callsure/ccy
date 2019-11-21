#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import random

list = []
module_path = os.path.dirname(__file__)
path = module_path + '/word/word.txt'
word_file = open(path, "r")
for line in word_file:
    list.append(str.rstrip(line))

def random_word(size):
    random.shuffle(list)
    temp_list = list
    if size <= 0:
        return temp_list[0:100]
    return temp_list[0:size]

