# -*- coding: utf-8 -*-

import os, time
from common.ElementParam import ElementParam
from common.Operate_pickle import readInfo, write
from common.Count import count_sum_false_cancel

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

def rerun(self, url, func):
    circle = 3
    while circle > 0:
        if circle == 3:
            func(self)
        else:
            if url != "":
                self.driver.get(url)
                time.sleep(1)
            func(self)
        info_data = readInfo(PATH("../log/" + ElementParam.INFO_FILE))
        if info_data[-1]['case_name'] == func.__name__ and info_data[-1]['result'] == '失败' and circle > 1:
            if os.path.exists(info_data[-1]['img']):
                os.remove(info_data[-1]['img'])
                print('删除错误截图')
            else:
                print('图片路径不存在')
            info_data.pop(-1)
            write(info_data, PATH("../log/" + ElementParam.INFO_FILE))
            count_sum_false_cancel(PATH("../log/" + ElementParam.SUM_FILE))   # 统计 总数减1 失败数减1
            self.logTest.checkPoint_false_cancel()  # checkPoint_减1
        elif info_data[-1]['case_name'] == func.__name__ and info_data[-1]['result'] == '通过':
            break
        circle -= 1


