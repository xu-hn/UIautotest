# -*- coding: utf-8 -*-

import os
import re
import time

#获取最新下载的文件夹的时间戳 or 把传入的str格式时间转化成时间戳
def to_time_stamp(f_time=0):
    if f_time == 0:
        directory = "C:\\Users\\Administrator\\Downloads\\"
        if os.path.isfile(directory):
            pass
        else:
            print("%s文件不存在" % directory)
        lists = os.listdir(directory)                                    #列出目录的下所有文件和文件夹保存到lists
        # L = [i for i in lists if re.findall(r'(download_.*?\.zip)', i)]  # 匹配以download开头 已经zip结尾的字符串
        L = [i for i in lists if re.findall(r'^(download||woven_qaoutput_qa_sink)_.*?\.zip$', i)]  # 匹配以download或woven_qaoutput_qa_sink开头 已经zip结尾的字符串
        L1 = [i for i in lists if re.findall(r'^(dir1-.*?\.woven$)', i)]
        L3 = [i for i in lists if re.findall(r'^(data.*?\.csv$)', i)]
        L = L + L1 + L3
        if not L:
            return False
        L.sort(key=lambda fn:os.path.getmtime(directory + "\\" + fn))  # 按时间排序
        file_new = os.path.join(directory,L[-1])                      # 获取最新的文件保存到file_new
        print('最新的文件为：',file_new)
        return os.path.getmtime(file_new)
    else:
        spt = time.strptime(f_time, "%Y-%m-%d%H:%M:%S") # 把strtime 转成strptime
        print(spt)
        text_time_stamp = time.mktime(spt) # 把strptime转化成时间戳
        print('转化后的时间戳：',text_time_stamp)
        return text_time_stamp

if __name__=="__main__":
    to_time_stamp()