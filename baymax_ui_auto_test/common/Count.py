# -*- coding: utf-8 -*-

from common.Operate_pickle import writeInfo, read, write, readInfo
from common.ElementParam import ElementParam
import os
import xlsxwriter
from common.XlsReport import OperateXls

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

def count_info(**kwargs):
    _info = {}
    step = ''
    check_step = ''

    for case in kwargs['testcase']:
        step = step + case['info'] + '\n'
    for check in kwargs['testcheck']:
        check_step = check_step + check['info'] + '\n'

    _info['step'] = step
    _info['check_step'] = check_step

    _info['id'] = kwargs['testinfo'][0]['id']
    _info['title'] = kwargs['testinfo'][0]['title']
    _info['name'] = kwargs['name']                 # 浏览器名字
    _info['case_name'] = kwargs['case_name']       # 执行用例的方法名
    _info['info'] = kwargs['testinfo'][0]['info']
    _info['msg']  = kwargs['testinfo'][0].get("msg", "")

    if kwargs['result']:
        _info['result'] = '通过'
        kwargs['logTest'].checkPointOK(caseName=kwargs["testinfo"][0]["title"],
                                       checkPoint=kwargs["case_name"] + "_" + kwargs["testinfo"][0].get( "msg", " "))
        _info["img"] = kwargs["logTest"].checkPointNG(driver=kwargs["driver"], caseName=kwargs["testinfo"][0]["title"],#用例通过添加截图
                                                      checkPoint=kwargs["case_name"] + "_" + kwargs["testinfo"][0].get("msg", " "))#
    elif not kwargs['result']:
        _info['result'] = '失败'
        # 错误截屏的路径
        print(kwargs["testinfo"][0].get("msg", "aaaaaa"))
        _info["img"] = kwargs["logTest"].checkPointNG(driver=kwargs["driver"], caseName=kwargs["testinfo"][0]["title"],
                                                      checkPoint=kwargs["case_name"] + "_" + kwargs["testinfo"][0].get("msg", " "))

    writeInfo(data=_info, path='../log/' + ElementParam.INFO_FILE)

def count_sum(result):
    data = {"sum": 0, "pass": 0, "fail": 0}
    _read = read("../log/" + ElementParam.SUM_FILE)
    if _read:
        data = _read
    data["sum"] += 1
    if result:
        data["pass"] += 1
    else:
        data["fail"] += 1
    write(data=data, path="../log/" + ElementParam.SUM_FILE)

def count_sum_false_cancel(result):
    # 失败后重跑 sum 减 1
    data = read("../log/" + ElementParam.SUM_FILE)
    data["sum"] -= 1
    data["fail"] -= 1
    write(data=data, path="../log/" + ElementParam.SUM_FILE)

def countDate(testDate, testSumDate):
    data = read(PATH("../log/" + ElementParam.SUM_FILE))
    if data:
        data["testDate"] = testDate
        data["testSumDate"] = testSumDate
        write(data=data, path=PATH("../log/" + ElementParam.SUM_FILE))
    else:
        print("统计数据失败")
    data = read(PATH("../log/" + ElementParam.SUM_FILE))
    print("==统计数据：%s==" % data)

def writeExcel():
    workbook = xlsxwriter.Workbook(PATH('../Report/' + ElementParam.REPORT_FILE))
    worksheet = workbook.add_worksheet("测试总况")
    worksheet2 = workbook.add_worksheet("测试详情")
    print
    operateXls = OperateXls(workbook)
    operateXls.init(worksheet, read(PATH("../log/" + ElementParam.SUM_FILE)))
    operateXls.detail(worksheet2, readInfo(PATH("../log/" + ElementParam.INFO_FILE)))
    operateXls.close()

if __name__ == "__main__":
    count_sum(False)