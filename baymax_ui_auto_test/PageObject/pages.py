# -*- coding: utf-8 -*-

from common.operate_element import OperateElement
from common.ErrorInfo import get_error_info
from common.ElementParam import ElementParam
from PageObject.CountResult import count_result
from time import sleep
import os
from common.Operate_str import *
import time
from common.operate_time import to_time_stamp
import re

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class PagesObjects:

    def __init__(self, kwargs):
        self.driver = kwargs['driver']              # driver
        if kwargs['testmsg'][1]['testinfo'][0].get('launch', 0) == 0:           # 刷新当前页面
            print('=======================================刷新了页面========================================')
            self.driver.refresh()
            time.sleep(1)

        self.operateElement = ""   # 操作元素的手柄
        self.isOperate = True     # 一个开关  默认为True operate失败时改为False  结果校验时 判断这个值为True就进行判断， 是False就不用校验结果
        self.testmsg = kwargs['testmsg']   # yaml读取的数据值
        self.logTest = kwargs['logTest']   # log对象 可以进行写log操作
        self.testInfo = kwargs['testmsg'][1]['testinfo']  # 用例的基本信息
        self.testcase = kwargs['testmsg'][1]['testcase']  # 元素的基本信息
        self.testcheck = kwargs['testmsg'][1]['check']  # 校验的基本信息
        self.caseName = kwargs['caseName']           # 用例的方法名称，unittest框架中的 test开头的方法名称
        self.get_value = []
        self.is_get = False

    def operate(self):
        if self.testmsg[0] is False:
            self.isOperate = False
            return False
        self.operateElement = OperateElement(self.driver)
        for i in self.testcase:
            self.rw_get_value(i)  # 读写容器操作
            result = self.operateElement.operate(i, self.testInfo, self.logTest)
            if not result['result']:
                msg = get_error_info({'type': ElementParam.DEFAULT_ERROR, 'element_info': i['element_info']})
                self.testInfo[0]['msg'] = msg
                self.isOperate = False
                return False
            if i.get('is_time', 0) != 0:
                sleep(i['is_time'])
            self.rw_get_value(i, result)  # 读写容器操作 并且打开开关
        return True

    def checkPoint(self):
        result = self.check()
        count_result(result=result, testcase=self.testcase, testcheck=self.testcheck, testinfo=self.testInfo,
                     name='chrome', case_name=self.caseName, logTest=self.logTest, driver=self.driver)

    def check(self):
        result = True
        if self.isOperate:
            for i in self.testcheck:
                self.rw_get_value(i)  # 执行读写容器操作

                try:
                    if i.get('expect_value', '888')[-3:] == '+拼接':
                        regex =".*拼接值(.*)\+拼.*"
                        matches = re.findall(regex, i['expect_value'])
                        if len(matches) == 1:
                            for match in matches:
                                print(match)
                                if match[:3] == "前+后":
                                    i['expect_value'] = i['expect_value'].split("拼接值")[0] + match[3:]
                                elif match[:3] == "后+前":
                                    if match == '后+前host':
                                        i['expect_value'] = ElementParam.HOST + i['expect_value'].split("拼接值")[0]
                                    else:
                                        i['expect_value'] = match[3:] + i['expect_value'].split("拼接值")[0]
                        else:
                            print('expect_value值没有被正则表达式匹配到，正则表达式匹配到的值为：', matches)
                            result = False
                            break
                except TypeError as msg:
                    print(msg)

                op_re = self.operateElement.operate(i, self.testInfo, self.logTest)

                if not op_re['result'] and (i.get('check', ElementParam.DEFAULT_CHECK) != ElementParam.CONTRARY):
                    msg = get_error_info({'type': ElementParam.DEFAULT_ERROR, 'element_info': i['element_info']})
                    self.testInfo[0]['msg'] = msg
                    return False


                # 默认检查点，检查元素存在
                if i.get('check', ElementParam.DEFAULT_CHECK) == ElementParam.DEFAULT_CHECK and not op_re['result']:
                    msg = get_error_info({"type": ElementParam.DEFAULT_CHECK, "element_info": i['element_info'], "info": i['info']})
                    self.testInfo[0]['msg'] = msg
                    result = False
                    return result

                L = [ElementParam.CONTRARY, ElementParam.VESSEL_CONTAIN_CURRENT, ElementParam.VESSEL_NOT_CONTAIN_CURRENT, ElementParam.CURRENT_CONTAIN_EXPECT, ElementParam.CURRENT_EQUAL_EXPECT,
                    ElementParam.VESSEL_NOT_CONTAIN_EXPECT, ElementParam.VESSEL_CONTAIN_EXPECT, ElementParam.DISPLAYED, ElementParam.NOT_DISPLAYED, ElementParam.TIME_DIFFERENCE,
                    ElementParam.CURRENT_NOT_EQUAL_EXPECT]
                if i.get("check", 'ooo') not in L and i.get('check', ElementParam.DEFAULT_CHECK) != ElementParam.DEFAULT_CHECK:
                    msg = get_error_info({'type': ElementParam.VALUE_ERROR, 'value': i['check'], 'info': i['info']})
                    self.testInfo[0]['msg'] = msg
                    result = False
                    break

                # 检查 元素不存在
                if i.get('check', ElementParam.DEFAULT_CHECK) == ElementParam.CONTRARY and op_re['result']:
                    msg = get_error_info({'type': ElementParam.CONTRARY, 'element': i['element_info'], 'info': i['info']})
                    self.testInfo[0]['msg'] = msg
                    result = False
                    break
                # 容器  包含  当前值
                if i.get('check', ElementParam.DEFAULT_CHECK) == ElementParam.VESSEL_CONTAIN_CURRENT and self.is_get and op_re.get("text", "ooooooo没获取到textoooooooo") not in self.get_value[i['expect_index']]:
                    msg = get_error_info({'type': ElementParam.VESSEL_CONTAIN_CURRENT, 'history': self.get_value, 'info': i['info'], 'current': op_re.get("text", "ooooooo没获取到textoooooooo")})
                    self.testInfo[0]['msg'] = msg
                    result = False
                    break
                # 容器 不包含 当前值
                if i.get('check', ElementParam.DEFAULT_CHECK) == ElementParam.VESSEL_NOT_CONTAIN_CURRENT and self.is_get and op_re['text'] in self.get_value[i['expect_index']]:
                    msg = get_error_info({'type': ElementParam.VESSEL_NOT_CONTAIN_CURRENT, 'history': self.get_value, 'info': i['info'], 'current': op_re['text']})
                    self.testInfo[0]['msg'] = msg
                    result = False
                    break
                # 当前值 包含 预期值
                if i.get('check', ElementParam.DEFAULT_CHECK) == ElementParam.CURRENT_CONTAIN_EXPECT and i.get('expect_value', 'ooo') not in op_re['text']:
                    msg = get_error_info({'type': ElementParam.CURRENT_CONTAIN_EXPECT, 'info': i['info'], 'get_value': op_re['text'], 'expect_value': i.get('expect_value', 'ooo')})
                    self.testInfo[0]['msg'] = msg
                    result = False
                    break
                # 当前值 等于 预期值
                if i.get('check', ElementParam.DEFAULT_CHECK) == ElementParam.CURRENT_EQUAL_EXPECT and op_re['text'] != i.get('expect_value', 'ooo'):
                    msg = get_error_info({'type': ElementParam.CURRENT_EQUAL_EXPECT, 'info': i['info'], 'get_attr': op_re['text'], 'expect_value': i.get('expect_value', 'ooo')})
                    self.testInfo[0]['msg'] = msg
                    result = False
                    break
                # 当前值 不等于 预期值
                if i.get('check', ElementParam.DEFAULT_CHECK) == ElementParam.CURRENT_NOT_EQUAL_EXPECT and op_re['text'] == i.get('expect_value', 'ooo'):
                    msg = get_error_info({'type': ElementParam.CURRENT_NOT_EQUAL_EXPECT, 'info': i['info'], 'get_attr': op_re['text'], 'expect_value': i.get('expect_value', 'ooo')})
                    self.testInfo[0]['msg'] = msg
                    result = False
                    break
                # 容器 不包含 预期值
                if i.get('check', ElementParam.DEFAULT_CHECK) == ElementParam.VESSEL_NOT_CONTAIN_EXPECT and self.is_get \
                        and contain_str(i['expect_value'], self.get_value, i.get('expect_index', 0)):
                    msg = get_error_info({'type': ElementParam.VESSEL_NOT_CONTAIN_EXPECT, 'history': self.get_value, 'info': i['info'], 'current': i['expect_value']})
                    self.testInfo[0]['msg'] = msg
                    result = False
                    break
                # 容器 包含 预期值
                if i.get('check', ElementParam.DEFAULT_CHECK) == ElementParam.VESSEL_CONTAIN_EXPECT and self.is_get \
                        and contain_not_str(i['expect_value'], self.get_value, i.get('expect_index', 0)):
                    msg = get_error_info({'type': ElementParam.VESSEL_CONTAIN_EXPECT, 'history': self.get_value, 'info': i['info'], 'current': i['expect_value']})
                    self.testInfo[0]['msg'] = msg
                    result = False
                    break
                # 检查页面元素显示  如果 不显示就返回False
                if i.get('check', ElementParam.DEFAULT_CHECK) == ElementParam.DISPLAYED and not op_re['result']:
                    msg = get_error_info({'type': ElementParam.DISPLAYED, 'info': i['info'], 'element': i['element_info']})
                    self.testInfo[0]['msg'] = msg
                    result = False
                    break
                # 检查页面元素不显示  如果 显示就返回False
                if i.get('check', ElementParam.DEFAULT_CHECK) == ElementParam.NOT_DISPLAYED and op_re['result']:
                    msg = get_error_info({'type': ElementParam.NOT_DISPLAYED, 'info': i['info'], 'element': i['element_info']})
                    self.testInfo[0]['msg'] = msg
                    result = False
                    break
                # 检查有时间差小于预期时间
                if i.get('check', ElementParam.DEFAULT_CHECK) == ElementParam.TIME_DIFFERENCE and (time.time() - to_time_stamp(f_time=op_re.get("text", 0))) > i.get('max_time', 5):
                    print(time.time() - to_time_stamp(f_time=op_re.get("text", 0)))
                    msg = get_error_info({'type': ElementParam.TIME_DIFFERENCE,  'info': i['info']})
                    self.testInfo[0]['msg'] = msg
                    result = False
                    break
                if i.get('is_time', 0) != 0:
                    sleep(i['is_time'])
        else:
            result = False
        return result

    # 读写容器
    def rw_get_value(self, i, result={}):
        '''
        :param i:  YAML文件传入的参数
        :param result:  是否执行的开关
        :return:
        '''
        if str(i.get('msg', ''))[-4:] == '+随机数':
                i['msg'] = random_str(i['msg'])
                self.get_value.append(i['msg'])
        if i.get('element_info', '')[-4:] == '+随机数':
            if i['find_type'] == 'name':
                i['element_info'] = self.get_value[int(i['v_index'])]
            if i['find_type'] == 'xpath':
                i['element_info'] = i['element_info'][: -4] % self.get_value[int(i['v_index'])]
        if i.get('element_info', '')[-3:] == '+拼接':
            if i['find_type'] == 'name':
                i['element_info'] = self.get_value[int(i['v_index'])] + i['join_value']
            if i['find_type'] == 'xpath':
                i['element_info'] = i['element_info'][: -3] % (self.get_value[int(i['v_index'])] + i['join_value'])
        # result 开关被打开
        if (i.get('operate_type', 0) == ElementParam.GET_TEXT or i.get('operate_type', 0) == ElementParam.GET_VALUE or \
                                i.get('operate_type', 0) == ElementParam.GET_ATTR) and result.get('result', False):
            self.get_value.append(result['text'])
            self.is_get = True


if __name__ == "__main__":
    from selenium import webdriver
    from common.Logger import myLog
    from common.operate_yaml import getYaml
    driver = webdriver.Chrome()
    driver.get('http://192.168.1.189:8515/#/login')
    logTest = myLog.getLog("chrome")
    testmsg = getYaml(PATH('../YAML/login/login'))
    kw = {'driver': driver, 'logTest': logTest, 'testmsg': testmsg}
    po = PagesObjects(kw)
    a = po.operate()
    print('aaaaaaaa::', a)