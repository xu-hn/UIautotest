# -*- coding: utf-8 -*-

from PageObject.data_monitor_page.operational_monitoring_page.operational_monitoring_page import OperationalMonitoringPage
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

# 运维管控页 测试
class OperationalMonitoringTest(ParametrizedTestCase):
    operational_url = ElementParam.OPERATIONAL_URL

    def login(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH(who_login(self.who)),
               "caseName": sys._getframe().f_code.co_name}
        page = LoginTestPage(app)
        page.operate()

    def to_resource_dir(self):
        self.login()
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/运维管控.yaml"),
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

    # 校验“运维监控-集群详情-页面校验”
#     @get_url()
#     def test_a089_operational_monitoring_cluster_detail(self):
#         self.to_resource_dir()
#         app = {"logTest": self.logTest, "driver": self.driver,
#                "path": PATH("../YAML/data_monitor_yaml/operational_monitoring_yaml/运维监控-集群详情-页面校验.yaml"),
#                "caseName": sys._getframe().f_code.co_name}
#         page = OperationalMonitoringPage(app)
#         page.operate()
#         page.check_point()
    
    # 校验“运维监控-节点状态-详情分析”
    @get_url()#operational_url
    def test_a90_operational_monitoring_detail_analyze(self):
        self.to_resource_dir()
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_monitor_yaml/operational_monitoring_yaml/运维监控-节点状态-详情分析.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = OperationalMonitoringPage(app)
        page.operate()
        page.check_point()
    
    # 校验“运维监控-数据源状态”
    @get_url(operational_url)
    def test_a91_operational_monitoring_detail_view(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_monitor_yaml/operational_monitoring_yaml/运维监控-数据源状态.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = OperationalMonitoringPage(app)
        page.operate()
        page.check_point()
    
    # 校验“运维监控-数据源状态_详情”
    @get_url()
    def test_a92_operational_monitoring_detail_view_detail(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_monitor_yaml/operational_monitoring_yaml/运维监控-数据源状态_详情.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = OperationalMonitoringPage(app)
        page.operate()
        page.check_point()
    
    # 校验“运维监控-数据源状态_详情_数据源点击”
    @get_url(operational_url)
    def test_a93_operational_monitoring_detail_view_detail_back(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_monitor_yaml/operational_monitoring_yaml/运维监控-数据源状态_详情_数据源点击.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = OperationalMonitoringPage(app)
        page.operate()
        page.check_point()
    
    # 校验“运维监控-数据源状态-查看全部_详情_删除”
    @get_url(operational_url)
    def test_a94_operational_monitoring_detail_view_detail_delete(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_monitor_yaml/operational_monitoring_yaml/运维监控-数据源状态-查看全部_详情_删除.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = OperationalMonitoringPage(app)
        page.operate()
        page.check_point()
    
    @classmethod
    def setUpClass(cls):
        super(OperationalMonitoringTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(OperationalMonitoringTest, cls).tearDownClass()




###################  ----------------------------------------------------=========================调试区===========================--------------------------------------------------------------

# 运维管控页 测试
class OperationalMonitoringTest_SSSS(ParametrizedTestCase):
    operational_url = ElementParam.OPERATIONAL_URL

    def login(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/user_for_test/user_dir1.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = LoginTestPage(app)
        page.operate()

    def to_resource_dir(self):
        self.login()
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/运维管控.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = HomePage(app)
        page.operate()

    #链接到某url装饰器
    def get_url(to_url):
        def decorator(func):
            def wrapper(self, *args, **kwargs):
                self.driver.get(to_url)
                func(self, *args, **kwargs)
            return wrapper
        return decorator

    # 校验“运维监控-集群详情-页面校验”
    def test_a089_operational_monitoring_cluster_detail(self):
        self.to_resource_dir()
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_monitor_yaml/operational_monitoring_yaml/运维监控-集群详情-页面校验.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = OperationalMonitoringPage(app)
        page.operate()
        page.check_point()

    # 校验“运维监控-数据源状态-查看全部”
    @get_url(operational_url)
    def test_a91_operational_monitoring_detail_view(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_monitor_yaml/operational_monitoring_yaml/运维监控-数据源状态-查看全部.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = OperationalMonitoringPage(app)
        page.operate()
        page.check_point()

    # 校验“运维监控-数据源状态-查看全部_详情”
    def test_a92_operational_monitoring_detail_view_detail(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_monitor_yaml/operational_monitoring_yaml/运维监控-数据源状态-查看全部_详情.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = OperationalMonitoringPage(app)
        page.operate()
        page.check_point()

    @classmethod
    def setUpClass(cls):
        super(OperationalMonitoringTest_SSSS, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(OperationalMonitoringTest_SSSS, cls).tearDownClass()
