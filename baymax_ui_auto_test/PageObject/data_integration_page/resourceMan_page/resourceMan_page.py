# -*- coding: utf-8 -*-

from PageObject.pages import PagesObjects
from common.operate_yaml import getYaml

# 资源目录页
class ResourceManPage:

    def __init__(self, kwargs):
        _kwargs = {'driver': kwargs['driver'], 'logTest': kwargs['logTest'],
                   'testmsg': getYaml(kwargs['path']), 'caseName': kwargs['caseName']}
        self.page_obj = PagesObjects(_kwargs)

    def operate(self):
        self.page_obj.operate()

    def check_point(self):
        self.page_obj.checkPoint()