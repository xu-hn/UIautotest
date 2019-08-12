# -*- coding: utf-8 -*-

import random

# 字符串A 是否在字符串B 中 ，在 返回True
def contain_str(current='', history=[], att_index=0):
    try:
        att_index = int(att_index)
        result = list(map(str, history))
        if current in result[att_index]:
            return True
        else:
            return False
    except IndexError:
        print('++++++++++++索引错误++++++++++++++++++')
        return True

# 字符串A 是否在字符串B 中 ，不在 返回True
def contain_not_str(current='', history=[], attr_index=0):
    try:
        att_index = int(attr_index)
        result = list(map(str, history))
        if current in result[att_index]:
            return False
        else:
            return True
    except IndexError:
        print('++++++++++++索引错误++++++++++++++++++')
        return True
# 生成尾数为6位数字的 随机字符串
def random_str(value='+随机数'):
    L = []
    for i in range(6):
         rand_num = random.randint(0, 9)
         L.append(str(rand_num))
    return value[:-4]+''.join(L)

if __name__ == "__main__":
    a = 'aa+随机数'
    print(random_str(a))