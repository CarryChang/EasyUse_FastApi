#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/13 0013 13:20
# @Author  : CarryChang
# @Software: PyCharm
# @email: coolcahng@gmail.com
# @web ：CarryChang.top
def file_read(number,path):
    pos_val = []
    with open(path, 'r', encoding='utf-8') as content:
        for con1 in content.readlines()[:number]:
            pos_val.append(con1.strip())
    return pos_val
# if __name__ == '__main__':
#     number = 100
#     path = '1-1.txt'
#     content = file_read(number,path)
#     print(len(content))
#     print(content)