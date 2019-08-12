# -*- coding: utf-8 -*-

from PageObject.data_govern_page.schema_analyze_page.schema_analyze_page import SchemaAnalyzaPage
from common.BaseRunner import ParametrizedTestCase
from common.ElementParam import ElementParam
from PageObject.login.login_page import LoginTestPage
from PageObject.home.home_page import HomePage
import sys, os, time
from common.case_false_rerun import rerun
from common.login_who import who_login

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), p)
)

# 元数据分析页面测试
class SchemaAnalyzeTest(ParametrizedTestCase):
    schema_analyze_url = ElementParam.SCHEMA_ANALYZE_URL


    def login(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH(who_login(self.who)),
               "caseName": sys._getframe().f_code.co_name}
        page = LoginTestPage(app)
        page.operate()

    def to_resource_dir(self):
        self.login()
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/元数据分析.yaml"),
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

    # 校验“源数据分析-选择元数据-页面校验”
    @get_url()
    def test_a165_schemaanalyze_schema_page(self):
        self.to_resource_dir()
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_govern_yaml/schema_analyze_yaml/元数据分析-选择元数据-页面校验.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = SchemaAnalyzaPage(app)
        page.operate()
        page.check_point()

    # 校验“源数据分析-选择元数据-新建”
    @get_url(schema_analyze_url)
    def test_a166_schemaanalyze_schema_create(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_govern_yaml/schema_analyze_yaml/源数据分析-选择元数据-新建.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = SchemaAnalyzaPage(app)
        page.operate()
        page.check_point()

    # 校验“源数据分析-选择元数据-保存”
    @get_url(schema_analyze_url)
    def test_a167_schemaanalyze_schema_save(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_govern_yaml/schema_analyze_yaml/源数据分析-选择元数据-保存.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = SchemaAnalyzaPage(app)
        page.operate()
        page.check_point()

    @classmethod
    def setUpClass(cls):
        super(SchemaAnalyzeTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(SchemaAnalyzeTest, cls).tearDownClass()