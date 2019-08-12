from common.BaseRunner import ParametrizedTestCase
import os, sys, time
from PageObject.home.home_page import HomePage
from PageObject.login.login_page import LoginTestPage
from common.case_false_rerun import rerun
from common.login_who import who_login

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(os.path.dirname(__file__)), p)
)
class HomePageTest_Cab(ParametrizedTestCase):
    def login(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH(who_login(self.who)),
               "caseName": sys._getframe().f_code.co_name}
        page = LoginTestPage(app)
        page.operate()

    def get_url(to_url=""):
        def decorator(func):
            def wrapper(self, *args, **kwargs):
                if to_url != "":
                    self.driver.get(to_url)
                    time.sleep(1)
                rerun(self, to_url, func)
            return wrapper
        return decorator

    # 校验“资源目录”页面
    @get_url()
    def test_a002_resource_dir(self):
        self.login()
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/资源目录.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = HomePage(app)
        page.operate()
        page.check_point()

    # 校验“数据导入”
    @get_url()
    def test_a004_data_import(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/数据导入.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = HomePage(app)
        page.operate()
        page.check_point()

    # 校验“文件导入”
    @get_url()
    def test_a005_file_import(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/文件导入.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = HomePage(app)
        page.operate()
        page.check_point()

    # 校验“采集器”
    @get_url()
    def test_a006_file_import(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/采集器.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = HomePage(app)
        page.operate()
        page.check_point()

    # 校验 “数据治理--质量分析”
    @get_url()
    def test_a007_quality_analyze(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/质量分析.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = HomePage(app)
        page.operate()
        page.check_point()

    # 校验 “数据治理--血缘分析”
    @get_url()
    def test_a008_blood_analyze(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/血缘分析.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = HomePage(app)
        page.operate()
        page.check_point()

    # 校验 “数据治理--血缘分析”
    @get_url()
    def test_a009_schema_analyze(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/元数据分析.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = HomePage(app)
        page.operate()
        page.check_point()

    # 校验 “数据治理--流程管理”
    @get_url()
    def test_a010_flow_manage(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/流程管理.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = HomePage(app)
        page.operate()
        page.check_point()

    # 校验 “数据监控--运维管控”
    @get_url()
    def test_a011_operations_control(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/运维管控.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = HomePage(app)
        page.operate()
        page.check_point()


    # 校验 “数据监控--任务监控.yaml”
    @get_url()
    def test_a013_task_control(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/任务监控.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = HomePage(app)
        page.operate()
        page.check_point()


    @classmethod
    def setUpClass(cls):
        super(HomePageTest_Cab, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(HomePageTest_Cab, cls).tearDownClass()


class HomePageTest_Cab_SSSS(ParametrizedTestCase):
    def login(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/login/login.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = LoginTestPage(app)
        page.operate()

    def get_url(to_url=""):
        def decorator(func):
            def wrapper(self, *args, **kwargs):
                if to_url != "":
                    self.driver.get(to_url)
                    time.sleep(1)
                rerun(self, to_url, func)
            return wrapper
        return decorator

    # 校验“资源目录”页面
    @get_url()
    def test_a002_resource_dir(self):
        self.login()
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/资源目录.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = HomePage(app)
        page.operate()
        page.check_point()

    # 校验 “数据监控--运维管控”
    @get_url()
    def test_a011_operations_control(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/运维管控.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = HomePage(app)
        page.operate()
        page.check_point()

    # 校验 “数据监控--访问监控yaml”
    @get_url()
    def test_a012_inquiry_control(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/访问监控1.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = HomePage(app)
        page.operate()
        page.check_point()

    # 校验 “数据监控--任务监控.yaml”
    @get_url()
    def test_a013_task_control(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/任务监控.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = HomePage(app)
        page.operate()
        page.check_point()

    @classmethod
    def setUpClass(cls):
        super(HomePageTest_Cab, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(HomePageTest_Cab, cls).tearDownClass()