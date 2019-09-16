# -*- coding: utf-8 -*-

from common.BaseRunner import ParametrizedTestCase
import unittest, os, sys, time
from PageObject.home.home_page import HomePage
from PageObject.login.login_page import LoginTestPage
from common.case_false_rerun import rerun
from common.login_who import who_login

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(os.path.dirname(__file__)), p)
)
class HomePageTest(ParametrizedTestCase):
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

    # # 校验“文件管理”页面
    # @get_url()
    # def test_a003_file_manage(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/文件管理.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = HomePage(app)
    #     page.operate()
    #     page.check_point()

    # 校验“数据导入”
    @get_url()
    def test_a003_data_import(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/数据导入.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = HomePage(app)
        page.operate()
        page.check_point()

    # 校验“文件导入”
    @get_url()
    def test_a004_file_import(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/文件导入.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = HomePage(app)
        page.operate()
        page.check_point()

    # 校验“采集器”
    @get_url()
    def test_a005_file_import(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/采集器.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = HomePage(app)
        page.operate()
        page.check_point()

    # 校验 “数据治理--质量分析”
    @get_url()
    def test_a006_quality_analyze(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/质量分析.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = HomePage(app)
        page.operate()
        page.check_point()
        
     # 校验 “数据治理--元数据分析”
    @get_url()
    def test_a007_metadata_analyze(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/元数据分析.yaml"),
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

   

    # 校验 “数据分析--流程管理”
    @get_url()
    def test_a009_flow_manage(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/流程管理.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = HomePage(app)
        page.operate()
        page.check_point()
    
    # 校验“数据分析--交互式查询”
#     @get_url()
#     def test_a014_project_dir(self):
#         app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/交互式查询.yaml"),
#               "caseName": sys._getframe().f_code.co_name}
#         page = HomePage(app)
#         page.operate()
#         page.check_point()        
    # 校验 “数据分析--项目目录”
    @get_url()
    def test_a010_project_dir(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/项目目录.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = HomePage(app)
        page.operate()
        page.check_point()

    # 校验 “数据监控--运维管理”
#     @get_url()
#     def test_a011_operations_control(self):
#         app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/运维管控.yaml"),
#                 "caseName": sys._getframe().f_code.co_name}
#         page = HomePage(app)
#         page.operate()
#         page.check_point()

#     # 校验 “数据监控--访问监控yaml”
#     @get_url()
#     def test_a012_inquiry_control(self):
#         app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/访问监控1.yaml"),
#                "caseName": sys._getframe().f_code.co_name}
#         page = HomePage(app)
#         page.operate()
#         page.check_point()

    # 校验 “数据监控--任务监控.yaml”
    @get_url()
    def test_a013_task_control(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/任务监控.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = HomePage(app)
        page.operate()
        page.check_point()




    # # 校验 “实时计算--作业管理.yaml”
    # def test_a014_work_manage(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/作业管理.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = HomePage(app)
    #     page.operate()
    #     page.check_point()
    #
    # # 校验 “实时计算--作业运维.yaml”
    # def test_a015_work_operations(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/作业运维.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = HomePage(app)
    #     page.operate()
    #     page.check_point()
    #
    # # 校验 “实时计算--作业模板.yaml”
    # def test_a016_work_template(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/作业模板.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = HomePage(app)
    #     page.operate()
    #     page.check_point()
#校验 “权限管理-用户管理”
    @get_url()  
    def test_017a_role_manage(self):
        self.login()
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/角色管理.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = HomePage(app)
        page.operate()
        page.check_point()
    #校验 “权限管理-用户管理”
    @get_url()  
    def test_017b_user_manage(self):
        #self.login()
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/用户管理.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = HomePage(app)
        page.operate()
        page.check_point()
    @classmethod
    def setUpClass(cls):
        super(HomePageTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(HomePageTest, cls).tearDownClass()


class HomePageTest_SSSS(ParametrizedTestCase):
    def login(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/login/login.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = LoginTestPage(app)
        page.operate()

    #链接到某url装饰器
    def get_url(to_url=""):
        def decorator(func):
            def wrapper(self, *args, **kwargs):
                if to_url != "":
                    self.driver.get(to_url)
                    func(self, *args, **kwargs)
            return wrapper
        return decorator

    # 校验“资源目录”页面
    def test_a002_resource_dir(self):
        self.login()

    # 校验 “数据监控--访问监控yaml”
    def test_a012_inquiry_control(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/访问监控1.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = HomePage(app)
        page.operate()
        page.check_point()

    # 校验 “数据监控--任务监控.yaml”
    def test_a013_task_control(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/任务监控.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = HomePage(app)
        page.operate()
        page.check_point()

    @classmethod
    def setUpClass(cls):
        super(HomePageTest_SSSS, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(HomePageTest_SSSS, cls).tearDownClass()


if __name__ == "__main__":
    unittest.main()


