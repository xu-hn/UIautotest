# -*- coding: utf-8 -*-

from PageObject.pages import PagesObjects
from common.operate_yaml import getYaml

# 元数据分析页面
class SchemaAnalyzaPage:

    def __init__(self, kwargs):
        _kwargs = {'driver': kwargs['driver'], 'logTest': kwargs['logTest'],
                   'testmsg': getYaml(kwargs['path']), 'caseName': kwargs['caseName']}
        self.page_obj = PagesObjects(_kwargs)

    def operate(self):
        self.page_obj.operate()

    def check_point(self):
        self.page_obj.checkPoint()