# -*- coding: utf-8 -*-

from common.BaseRunner import ParametrizedTestCase
import unittest, os, sys, time
from PageObject.data_integration_page.collector_page.collector_page import CollectorPage
from PageObject.home.home_page import HomePage
from PageObject.login.login_page import LoginTestPage
from common.ElementParam import ElementParam
from common.case_false_rerun import rerun
from common.login_who import who_login


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), p)
)

# 采集器列表页
class CollectorTemplateTest(ParametrizedTestCase):
    def login(self):
        app = {"logTest": self.logTest, "driver": self.driver,  "path": PATH(who_login(self.who)),
               "caseName": sys._getframe().f_code.co_name}
        page = LoginTestPage(app)
        page.operate()

    def to_resource_dir(self):
        self.login()
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/采集器.yaml"),
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

    # 校验“注册采集器”
    @get_url()
    def test_a060_create_collector(self):
        self.to_resource_dir()
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/collector_yaml/collector_template_yaml/采集器-注册.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = CollectorPage(app)
        page.operate()
        page.check_point()

    # 校验“编辑采集器”
    @get_url()
    def test_a061_edit_collector(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/collector_yaml/collector_template_yaml/采集器-编辑.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = CollectorPage(app)
        page.operate()
        page.check_point()

     # 校验“删除采集器”
    @get_url()
    def test_a062_delete_collector(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/collector_yaml/collector_template_yaml/采集器-删除.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = CollectorPage(app)
        page.operate()
        page.check_point()

    @classmethod
    def setUpClass(cls):
        super(CollectorTemplateTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(CollectorTemplateTest, cls).tearDownClass()


# 采集器 导入任务页测试
class CollectorimportDataTest(ParametrizedTestCase):
    importData_url = ElementParam.IMPORT_DATA_URL
    def login(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH(who_login(self.who)),
               "caseName": sys._getframe().f_code.co_name}
        page = LoginTestPage(app)
        page.operate()

    def to_resource_dir(self):
        self.login()
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/采集器.yaml"),
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

    # 校验“校验导入任务页”
    @get_url()
    def test_a063_collector_import_data(self):
        self.to_resource_dir()
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_integration_yaml/collector_yaml/collector_import_data_yaml/采集器-导入任务-列表.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = CollectorPage(app)
        page.operate()
        page.check_point()

     # 校验“校验导入任务-同步任务信息”
    @get_url(importData_url)
    def test_a064_collector_import_data_sync(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_integration_yaml/collector_yaml/collector_import_data_yaml/采集器-导入任务-同步任务信息.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = CollectorPage(app)
        page.operate()
        page.check_point()

    # 校验“校验导入任务页-数据源表预览”
    @get_url(importData_url)
    def test_a065_collector_import_data_source(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_integration_yaml/collector_yaml/collector_import_data_yaml/采集器-导入任务-数据源表预览.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = CollectorPage(app)
        page.operate()
        page.check_point()

    # 校验“校验导入任务页-预览”
    @get_url(importData_url)
    def test_a066_collector_import_data_preview(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_integration_yaml/collector_yaml/collector_import_data_yaml/采集器-导入任务-预览.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = CollectorPage(app)
        page.operate()
        page.check_point()

    # 校验“校验导入任务页-预览-关闭”
    @get_url()
    def test_a067_collector_import_data_close(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_integration_yaml/collector_yaml/collector_import_data_yaml/采集器-导入任务-预览-关闭.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = CollectorPage(app)
        page.operate()
        page.check_point()

    # 校验“校验导入任务页-预览-确定”
    @get_url()
    def test_a068_collector_import_data_ok(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_integration_yaml/collector_yaml/collector_import_data_yaml/采集器-导入任务-预览-确定.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = CollectorPage(app)
        page.operate()
        page.check_point()

    # 校验“校验导入任务页-执行”
    @get_url()
    def test_a069_collector_import_data(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_integration_yaml/collector_yaml/collector_import_data_yaml/采集器-导入任务-执行.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = CollectorPage(app)
        page.operate()
        page.check_point()

    # 校验“校验导入任务-执行列表-查看日志”
    @get_url(importData_url)
    def test_a070_collector_import_data_view_log(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_integration_yaml/collector_yaml/collector_import_data_yaml/采集器-导入任务-执行列表-查看日志.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = CollectorPage(app)
        page.operate()
        page.check_point()

    # 校验“校验导入任务-执行列表-查看错误日志”
    @get_url(importData_url)
    def test_a071_collector_import_data_view_error_log(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_integration_yaml/collector_yaml/collector_import_data_yaml/采集器-导入任务-执行列表-查看错误日志.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = CollectorPage(app)
        page.operate()
        page.check_point()

    @classmethod
    def setUpClass(cls):
        super(CollectorimportDataTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(CollectorimportDataTest, cls).tearDownClass()


# 采集器 任务页测试
class CollectorTaskListTest(ParametrizedTestCase):
    view_url = ElementParam.VIEW_URL  # 详细信息页
    taskList_url = ElementParam.TASK_LIST_URL  # 任务列表页
    dir_url = ElementParam.DIR_URL     # 资源目录页

    def login(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH(who_login(self.who)),
               "caseName": sys._getframe().f_code.co_name}
        page = LoginTestPage(app)
        page.operate()

    def to_resource_dir(self):
        self.login()
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/采集器.yaml"),
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

    # 校验“校验采集器-资源目录-页面校验”
    @get_url()
    def test_a072_collector_dir(self):
        self.to_resource_dir()
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_integration_yaml/collector_yaml/collector_task_list_yaml/采集器-资源目录-页面校验.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = CollectorPage(app)
        page.operate()
        page.check_point()

    # # 校验“校验采集器-资源目录-同步”
    # @get_url(dir_url)
    # def test_a073_collector_dir_sync(self):
    #     app = {"logTest": self.logTest, "driver": self.driver,
    #            "path": PATH("../YAML/data_integration_yaml/collector_yaml/collector_task_list_yaml/采集器-资源目录-同步.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = CollectorPage(app)
    #     page.operate()
    #     page.check_point()

    # 校验“校验采集器-详细信息-页面校验”
    @get_url(view_url)
    def test_a074_collector_detail(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_integration_yaml/collector_yaml/collector_task_list_yaml/采集器-详细信息-页面校验.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = CollectorPage(app)
        page.operate()
        page.check_point()

    # 校验“校验采集器-任务列表-页面校验”
    @get_url()
    def test_a075_collector_task_list(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_integration_yaml/collector_yaml/collector_task_list_yaml/采集器-任务列表-页面校验.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = CollectorPage(app)
        page.operate()
        page.check_point()

    # 校验“校验采集器-任务列表-新建任务”
    @get_url(view_url)
    def test_a076_collector_task_list_create(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_integration_yaml/collector_yaml/collector_task_list_yaml/采集器-任务列表-新建任务.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = CollectorPage(app)
        page.operate()
        page.check_point()

    # 校验“校验采集器-任务列表-复制”
    @get_url(taskList_url)
    def test_a077_collector_task_list_copy(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_integration_yaml/collector_yaml/collector_task_list_yaml/采集器-任务列表-复制.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = CollectorPage(app)
        page.operate()
        page.check_point()

    # 校验“校验采集器-任务列表-启动”
    @get_url(taskList_url)
    def test_a078_collector_task_list_start(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_integration_yaml/collector_yaml/collector_task_list_yaml/采集器-任务列表-启动.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = CollectorPage(app)
        page.operate()
        page.check_point()

    # 校验“校验采集器-任务列表-停用”
    @get_url()
    def test_a079_collector_task_list_stop(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_integration_yaml/collector_yaml/collector_task_list_yaml/采集器-任务列表-停用.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = CollectorPage(app)
        page.operate()
        page.check_point()

    # 校验“校验采集器-任务列表-删除”
    @get_url()
    def test_a080_collector_task_list_delete(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_integration_yaml/collector_yaml/collector_task_list_yaml/采集器-任务列表-删除.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = CollectorPage(app)
        page.operate()
        page.check_point()

    # 校验“校验采集器-任务列表-同步任务信息”
    @get_url()
    def test_a081_collector_task_list_sync(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_integration_yaml/collector_yaml/collector_task_list_yaml/采集器-任务列表-同步任务信息.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = CollectorPage(app)
        page.operate()
        page.check_point()

     # 校验“校验采集器-任务列表-数据源表预览”
    @get_url()
    def test_a082_collector_task_list_view(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_integration_yaml/collector_yaml/collector_task_list_yaml/采集器-任务列表-数据源表预览.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = CollectorPage(app)
        page.operate()
        page.check_point()

    # 校验“校验采集器-任务列表-执行列表”
    @get_url()
    def test_a083_collector_task_list_execute(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_integration_yaml/collector_yaml/collector_task_list_yaml/采集器-任务列表-执行列表.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = CollectorPage(app)
        page.operate()
        page.check_point()

    # 校验“校验采集器-任务列表-执行列表-查看日志”
    @get_url(taskList_url)
    def test_a084_collector_task_list_execute_view_log(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_integration_yaml/collector_yaml/collector_task_list_yaml/采集器-任务列表-执行列表-查看日志.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = CollectorPage(app)
        page.operate()
        page.check_point()

    # 校验“校验采集器-任务列表-执行列表-查看错误日志”
    @get_url(taskList_url)
    def test_a085_collector_task_list_execute_view_err_log(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_integration_yaml/collector_yaml/collector_task_list_yaml/采集器-任务列表-执行列表-查看错误日志.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = CollectorPage(app)
        page.operate()
        page.check_point()

    # 校验“校验采集器-任务列表-执行列表-预览数据集”
    @get_url(taskList_url)
    def test_a086_collector_task_list_execute_preview(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_integration_yaml/collector_yaml/collector_task_list_yaml/采集器-任务列表-执行列表-预览数据集.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = CollectorPage(app)
        page.operate()
        page.check_point()

    # 校验“校验采集器-任务列表-执行列表-预览数据集-关闭”
    @get_url()
    def test_a087_collector_task_list_execute_preview_close(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_integration_yaml/collector_yaml/collector_task_list_yaml/采集器-任务列表-执行列表-预览数据集-关闭.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = CollectorPage(app)
        page.operate()
        page.check_point()

    # 校验“校验采集器-任务列表-执行列表-预览数据集-确定”
    @get_url()
    def test_a088_collector_task_list_execute_preview_ok(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_integration_yaml/collector_yaml/collector_task_list_yaml/采集器-任务列表-执行列表-预览数据集-确定.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = CollectorPage(app)
        page.operate()
        page.check_point()

    @classmethod
    def setUpClass(cls):
        super(CollectorTaskListTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(CollectorTaskListTest, cls).tearDownClass()





###### ----------------------------------------------------------=========================调试区=======================---------------------------------------------------------

# 采集器列表页
class CollectorTemplateTest_SSSS(ParametrizedTestCase):
    def login(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH(who_login(self.who)),
               "caseName": sys._getframe().f_code.co_name}
        page = LoginTestPage(app)
        page.operate()

    def to_resource_dir(self):
        self.login()
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/采集器.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = HomePage(app)
        page.operate()


        # 校验“注册采集器”
    def test_a060_create_collector(self):
        self.to_resource_dir()
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/collector_yaml/collector_template_yaml/采集器-注册.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = CollectorPage(app)
        page.operate()
        page.check_point()

    # 校验“编辑采集器”
    def test_a061_edit_collector(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/collector_yaml/collector_template_yaml/采集器-编辑.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = CollectorPage(app)
        page.operate()
        page.check_point()

     # 校验“删除采集器”
    def test_a062_delete_collector(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/collector_yaml/collector_template_yaml/采集器-删除.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = CollectorPage(app)
        page.operate()
        page.check_point()

    @classmethod
    def setUpClass(cls):
        super(CollectorTemplateTest_SSSS, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(CollectorTemplateTest_SSSS, cls).tearDownClass()

# 采集器 导入任务页测试
class CollectorimportDataTest_SSSS(ParametrizedTestCase):
    importData_url = ElementParam.IMPORT_DATA_URL
    def login(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH(who_login(self.who)),
               "caseName": sys._getframe().f_code.co_name}
        page = LoginTestPage(app)
        page.operate()

    def to_resource_dir(self):
        self.login()
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/采集器.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = HomePage(app)
        page.operate()

    #链接到某url装饰器
    def get_url(to_url=""):
        def decorator(func):
            def wrapper(self, *args, **kwargs):
                if to_url != "":
                    self.driver.get(to_url)
                    time.sleep(1)
                rerun(self, to_url, func)
            return wrapper
        return decorator

    # 校验“校验导入任务页”
    @get_url()
    def test_a063_collector_import_data(self):
        self.to_resource_dir()
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_integration_yaml/collector_yaml/collector_import_data_yaml/采集器-导入任务-列表.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = CollectorPage(app)
        page.operate()
        page.check_point()

    #       # 校验“校验导入任务页-预览-确定”
    # def test_a068_collector_import_data_ok(self):
    #     app = {"logTest": self.logTest, "driver": self.driver,
    #            "path": PATH("../YAML/data_integration_yaml/collector_yaml/collector_import_data_yaml/采集器-导入任务-预览-确定.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = CollectorPage(app)
    #     page.operate()
    #     page.check_point()
    #
    # # 校验“校验导入任务页-执行”
    # def test_a069_collector_import_data(self):
    #     app = {"logTest": self.logTest, "driver": self.driver,
    #            "path": PATH("../YAML/data_integration_yaml/collector_yaml/collector_import_data_yaml/采集器-导入任务-执行.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = CollectorPage(app)
    #     page.operate()
    #     page.check_point()

    # 校验“校验导入任务-执行列表-查看日志”
    @get_url(importData_url)
    def test_a070_collector_import_data_view_log(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_integration_yaml/collector_yaml/collector_import_data_yaml/采集器-导入任务-执行列表-查看日志.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = CollectorPage(app)
        page.operate()
        page.check_point()

    # # 校验“校验导入任务-执行列表-查看错误日志”
    # @get_url(importData_url)
    # def test_a071_collector_import_data_view_error_log(self):
    #     app = {"logTest": self.logTest, "driver": self.driver,
    #            "path": PATH("../YAML/data_integration_yaml/collector_yaml/collector_import_data_yaml/采集器-导入任务-执行列表-查看错误日志.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = CollectorPage(app)
    #     page.operate()
    #     page.check_point()
    #
    #
    # # 校验“校验导入任务-执行列表-查看错误日志”
    # @get_url(importData_url)
    # def test_a072_collector_import_data_view_error_log(self):
    #     app = {"logTest": self.logTest, "driver": self.driver,
    #            "path": PATH("../YAML/data_integration_yaml/collector_yaml/collector_import_data_yaml/采集器-导入任务-执行列表-查看错误日志.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = CollectorPage(app)
    #     page.operate()
    #     page.check_point()

    @classmethod
    def setUpClass(cls):
        super(CollectorimportDataTest_SSSS, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(CollectorimportDataTest_SSSS, cls).tearDownClass()


# 采集器 任务页测试
class CollectorTaskListTest_SSSS(ParametrizedTestCase):
    view_url = ElementParam.VIEW_URL  # 详细信息页
    taskList_url = ElementParam.TASK_LIST_URL  # 任务列表页
    dir_url = ElementParam.DIR_URL     # 资源目录页

    def login(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH(who_login(self.who)),
               "caseName": sys._getframe().f_code.co_name}
        page = LoginTestPage(app)
        page.operate()

    def to_resource_dir(self):
        self.login()
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/采集器.yaml"),
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

    # 校验“校验采集器-资源目录-页面校验”
    def test_a072_collector_dir(self):
        self.to_resource_dir()

    @get_url(view_url)
    def test_a076_collector_task_list_create(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_integration_yaml/collector_yaml/collector_task_list_yaml/采集器-任务列表-新建任务.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = CollectorPage(app)
        page.operate()
        page.check_point()


    @classmethod
    def setUpClass(cls):
        super(CollectorTaskListTest_SSSS, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(CollectorTaskListTest_SSSS, cls).tearDownClass()

