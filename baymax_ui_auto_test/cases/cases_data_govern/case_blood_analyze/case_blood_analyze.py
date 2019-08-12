# -*- coding: utf-8 -*-

from PageObject.data_govern_page.blood_analyze_page.blood_analyze_page import BloodAnalyzaPage
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

# 血缘分析页面测试
class BloodAnalyzeTest(ParametrizedTestCase):
    blood_analyze_url = ElementParam.BLOOD_ANALYZE_URL

    def login(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH(who_login(self.who)),
               "caseName": sys._getframe().f_code.co_name}
        page = LoginTestPage(app)
        page.operate()

    def to_resource_dir(self):
        self.login()
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/血缘分析.yaml"),
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

    # 校验“血缘分析-打开数据集-页面校验”
    @get_url()
    def test_a161_bloodanalyze_opendataset_page(self):
        self.to_resource_dir()
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_govern_yaml/blood_analyze_yaml/血缘分析-打开数据集-页面校验.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = BloodAnalyzaPage(app)
        page.operate()
        page.check_point()

    # 校验“血缘分析-打开数据集-查看子集”
    @get_url(blood_analyze_url)
    def test_a162_bloodanalyze_opendataset_subset(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_govern_yaml/blood_analyze_yaml/血缘分析-打开数据集-查看子集.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = BloodAnalyzaPage(app)
        page.operate()
        page.check_point()

    # 校验“血缘分析-打开数据集-查看父集”
    @get_url(blood_analyze_url)
    def test_a163_bloodanalyze_opendataset_superset(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_govern_yaml/blood_analyze_yaml/血缘分析-打开数据集-查看父集.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = BloodAnalyzaPage(app)
        page.operate()
        page.check_point()

    # 校验“血缘分析-打开数据集-关闭父集”
    @get_url(blood_analyze_url)
    def test_a164_bloodanalyze_opendataset_close_superset(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_govern_yaml/blood_analyze_yaml/血缘分析-打开数据集-关闭父集.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = BloodAnalyzaPage(app)
        page.operate()
        page.check_point()

    @classmethod
    def setUpClass(cls):
        super(BloodAnalyzeTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(BloodAnalyzeTest, cls).tearDownClass()