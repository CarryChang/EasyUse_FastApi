#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/13 0013 20:08
# @Author  : CarryChang
# @Software: PyCharm
# @email: coolcahng@gmail.com
# @web ：CarryChang.top
path_list = ['neg_all.txt', 'pos_all.txt']
train_all = open('train_all.txt', 'w', encoding='utf-8')
for path in path_list:
    if 'pos' in path:
        with open(path, 'r', encoding='utf-8') as file:
            for content in file:
                train_all.write('5'+'\t'+content.strip() + '\n')
    else:
        with open(path, 'r', encoding='utf-8') as file:
            for content in file:
                train_all.write('1' + '\t' + content.strip() + '\n')
train_all.close()
