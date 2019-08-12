# -*- coding: utf-8 -*-

from PageObject.pages import PagesObjects
from common.operate_yaml import getYaml

'''
登录页面
'''
class LoginTestPage:

    def __init__(self, kwargs):
        _kwargs = {'driver': kwargs['driver'], 'logTest': kwargs['logTest'],
                   'testmsg': getYaml(kwargs['path']), 'caseName': kwargs['caseName']}
        self.page_obj = PagesObjects(_kwargs)

    def operate(self):
        self.page_obj.operate()

    def check_point(self):
        self.page_obj.checkPoint()


if __name__ =='__main__':
    from selenium import webdriver
    from common.Logger import myLog

    driver = webdriver.Chrome()
    driver.get('http://192.168.1.189:8515/#/login')
    logTest = myLog.getLog("chrome")
    PATH = ('D:/project/baymax_ui_auto_test/YAML/login/login')
    kw = {'driver': driver, 'logTest': logTest, 'path': PATH}
    tester = LoginTestPage(kw)
    tester.operate()
