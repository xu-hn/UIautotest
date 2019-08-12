# -*- coding: utf-8 -*-

from common.OperateFile import remove_file, mkdir_file
from common.ElementParam import ElementParam
from common.Operate_pickle import read,write
import os


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

# 删除 Element的info.pickle文件 和 sum.pickle文件
def destroy():
    remove_file(PATH("../log/"+ElementParam.INFO_FILE))
    remove_file(PATH("../log/"+ElementParam.SUM_FILE))

def mk_file():
    '''
    1.删除 info.pickle文件 和 sum.pickle文件
    2. 创建info.pickle文件 和 sum.pickle文件
    3. 把data 写入sum.pickle文件
    '''
    destroy()
    mkdir_file(PATH("../log/"+ElementParam.INFO_FILE))
    mkdir_file(PATH("../log/"+ElementParam.SUM_FILE))

    data = read(PATH("../log/"+ElementParam.INFO_FILE))

    data["version"] = ElementParam.VERSION
    data["sum"] = 0
    data["pass"] = 0
    data["fail"] = 0
    write(data=data, path=PATH("../log/"+ElementParam.SUM_FILE))
