# -*- coding: utf-8 -*-

from common.BaseRunner import ParametrizedTestCase
import unittest, os, sys, time
from PageObject.data_integration_page.file_import_page.file_import_page import FileImportPage
from PageObject.home.home_page import HomePage
from PageObject.login.login_page import LoginTestPage
from common.case_false_rerun import rerun
from common.login_who import who_login

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), p)
)

class FileImportTest(ParametrizedTestCase):
    def login(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH(who_login(self.who)),
               "caseName": sys._getframe().f_code.co_name}
        page = LoginTestPage(app)
        page.operate()

    def to_resource_dir(self):
        self.login()
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/文件导入.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = HomePage(app)
        page.operate()

    def get_url(to_url=""):
        # 连接到某个url且失败重跑的装饰器
        def decorator(func):
            def wrapper(self, *args, **kwargs):
                if to_url != "":
                    self.driver.get(to_url)
                    time.sleep(1)
                rerun(self, to_url, func)
            return wrapper
        return decorator

    # 校验“创建文件导入任务”
    @get_url()
    def test_a058_create_file_import(self):
        self.to_resource_dir()
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/file_import_yaml/文件导入-创建.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FileImportPage(app)
        page.operate()
        page.check_point()

    # 校验“复制文件导入任务”
    @get_url()
    def test_a059_copy_file_import(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/file_import_yaml/文件导入-复制.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FileImportPage(app)
        page.operate()
        page.check_point()

    @classmethod
    def setUpClass(cls):
        super(FileImportTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(FileImportTest, cls).tearDownClass()