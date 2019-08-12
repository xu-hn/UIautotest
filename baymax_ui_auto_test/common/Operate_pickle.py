# -*- coding: utf-8 -*-

import pickle

def readInfo(path):
    with open(path, 'rb') as f:
        try:
            data = pickle.load(f)
        except EOFError:
            data = []
    return data

def writeInfo(data, path):
    _read = readInfo(path)
    result = []
    if _read:
        _read.append(data)
        result = _read
    else:
        result.append(data)
    with open(path, 'wb') as f:
        pickle.dump(result, f)

def read(path):
    data = {}
    with open(path, 'rb') as f:
        try:
            data = pickle.load(f)
        except EOFError:
            data = {}
            # print("读取文件错误")
    return data

# pickle文件写入信息
def write(data, path="data.pickle"):
    with open(path, 'wb') as f:
        pickle.dump(data, f, 0)



if __name__ == "__main__":
    print(read('../log/' + 'sum.pickle'))
    print(readInfo('../log/' + 'info.pickle'))