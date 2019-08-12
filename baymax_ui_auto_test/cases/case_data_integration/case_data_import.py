# -*- coding: utf-8 -*-

from common.BaseRunner import ParametrizedTestCase
import unittest, os, sys, time
from PageObject.data_integration_page.data_import_page.data_import_page import DataImportPage
from PageObject.home.home_page import HomePage
from PageObject.login.login_page import LoginTestPage
from common.case_false_rerun import rerun
from common.ElementParam import ElementParam
from common.login_who import who_login

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(os.path.dirname(__file__)), p)
)

class DataImportTest(ParametrizedTestCase):
    data_import_url = ElementParam.HOST + '/#/synchronization'
    def login(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH(who_login(self.who)),
               "caseName": sys._getframe().f_code.co_name}
        page = LoginTestPage(app)
        page.operate()

    def to_resource_dir(self):
        self.login()
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/数据导入.yaml"),
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

    # 校验“数据导入-创建”任务
    @get_url()
    def test_a043_create_data_import(self):
        self.to_resource_dir()
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/data_import_yaml/数据导入-创建.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DataImportPage(app)
        page.operate()
        page.check_point()

    # 校验“数据导入-复制”任务
    @get_url()
    def test_a044_copy_data_import(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/data_import_yaml/数据导入-复制.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DataImportPage(app)
        page.operate()
        page.check_point()

    # 校验“数据导入-启用”任务
    @get_url()
    def test_a053_start_data_import(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/data_import_yaml/数据导入-启用.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DataImportPage(app)
        page.operate()
        page.check_point()

    # 校验“数据导入-执行列表”任务
    @get_url(data_import_url)
    def test_a054_execute_list_data_import(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/data_import_yaml/数据导入-执行列表.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DataImportPage(app)
        page.operate()
        page.check_point()

    # 校验“数据导入-预览数据集”任务
    @get_url(data_import_url)
    def test_a055_preview_data_import(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/data_import_yaml/数据导入-预览数据集.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DataImportPage(app)
        page.operate()
        page.check_point()

    # 校验“数据导入-停用”任务
    @get_url(data_import_url)
    def test_a056_stop_data_import(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/data_import_yaml/数据导入-停用.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DataImportPage(app)
        page.operate()
        page.check_point()

    # 校验“数据导入-删除”任务
    @get_url()
    def test_a057_delete_data_import(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/data_import_yaml/数据导入-删除.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DataImportPage(app)
        page.operate()
        page.check_point()

    @classmethod
    def setUpClass(cls):
        super(DataImportTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(DataImportTest, cls).tearDownClass()

# ---------------------------------------------------------------------- 调试区 --------------------------------------------------------------------------------
class DataImportTest_SSSS(ParametrizedTestCase):
    data_import_url = ElementParam.HOST + '/#/synchronization'
    def login(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/user_for_test/user_dir1.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = LoginTestPage(app)
        page.operate()

    def to_resource_dir(self):
        self.login()
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/数据导入.yaml"),
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

    # 校验“数据导入-创建”任务
    @get_url()
    def test_a043_create_data_import(self):
        self.to_resource_dir()
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/data_import_yaml/数据导入-创建.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = DataImportPage(app)
        page.operate()
        page.check_point()

    @classmethod
    def setUpClass(cls):
        super(DataImportTest_SSSS, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(DataImportTest_SSSS, cls).tearDownClass()


if __name__ == "__main__":
    unittest.main()

