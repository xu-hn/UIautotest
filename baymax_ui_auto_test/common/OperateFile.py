# -*- coding: utf-8 -*-

import os

# 删除文件
def remove_file(f):
    if os.path.isfile(f):
        os.remove(f)
    else:
        print("%s文件不存在，无法删除" % f)


# 创建文件
def mkdir_file(f, method='w+'):
    if not os.path.isfile(f):
        with open(f, method, encoding="utf-8") as fs:
            print("创建文件%s成功" % f)
            pass
    else:
        print("%s文件已经存在，创建失败" % f)
        pass
#清除指定路径下包含某个字符的所有文件    
def remove_path_key_file(key,path):
    ls = os.listdir(path)
    print(ls)
    for i in ls :
        if key in i :
            os.remove(path+'\\'+i) 

