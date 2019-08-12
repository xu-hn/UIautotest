# -*- coding: utf-8 -*-

from PageObject.data_monitor_page.task_control_page.task_control_page import TaskControlPage
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

# 任务监控页面测试
class TaskControlTest(ParametrizedTestCase):
    task_control_url = ElementParam.TASK_CONTROL_URL

    def login(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH(who_login(self.who)),
               "caseName": sys._getframe().f_code.co_name}
        page = LoginTestPage(app)
        page.operate()

    def to_resource_dir(self):
        self.login()
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/任务监控.yaml"),
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

    # 校验“任务监控-任务完成情况-详情”
    @get_url()
    def test_a095_taskControl_completion_detail(self):
        self.to_resource_dir()
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_monitor_yaml/task_control_yaml/任务监控-任务完成情况-详情.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = TaskControlPage(app)
        page.operate()
        page.check_point()

    # 校验“任务监控-任务完成情况-详情-归类信息”
    @get_url(task_control_url)
    def test_a096_taskControl_completion_detail_categorize_information(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_monitor_yaml/task_control_yaml/任务监控-任务完成情况-详情_归类信息.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = TaskControlPage(app)
        page.operate()
        page.check_point()

    # 校验“任务监控-任务完成情况-详情-概率分析”
    @get_url(task_control_url)
    def test_a097_taskControl_completion_detail_probability_analysis(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_monitor_yaml/task_control_yaml/任务监控-任务完成情况-详情_概率分析.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = TaskControlPage(app)
        page.operate()
        page.check_point()

    # 校验“任务监控-任务完成情况-运行中”
    @get_url(task_control_url)
    def test_a098_taskControl_completion_detail_run(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_monitor_yaml/task_control_yaml/任务监控-任务完成情况-运行中.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = TaskControlPage(app)
        page.operate()
        page.check_point()

    # 校验“任务监控-任务完成情况-等待”
    @get_url(task_control_url)
    def test_a099_taskControl_completion_detail_ready(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_monitor_yaml/task_control_yaml/任务监控-任务完成情况-等待.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = TaskControlPage(app)
        page.operate()
        page.check_point()

    # 校验“任务监控-任务完成情况-成功”
    @get_url(task_control_url)
    def test_a100_taskControl_completion_detail_success(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_monitor_yaml/task_control_yaml/任务监控-任务完成情况-成功.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = TaskControlPage(app)
        page.operate()
        page.check_point()

    # 校验“任务监控-任务完成情况-成功-删除”
    @get_url(task_control_url)
    def test_a101_taskControl_completion_detail_success_delete(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_monitor_yaml/task_control_yaml/任务监控-任务完成情况-成功-删除.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = TaskControlPage(app)
        page.operate()
        page.check_point()

    # 校验“任务监控-任务完成情况-失败”
    @get_url(task_control_url)
    def test_a102_taskControl_completion_detail_fail(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_monitor_yaml/task_control_yaml/任务监控-任务完成情况-失败.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = TaskControlPage(app)
        page.operate()
        page.check_point()

    # 校验“任务监控-任务完成情况-失败-删除”
    @get_url(task_control_url)
    def test_a103_taskControl_completion_detail_fail_delete(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_monitor_yaml/task_control_yaml/任务监控-任务完成情况-失败-删除.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = TaskControlPage(app)
        page.operate()
        page.check_point()

    # 校验“任务监控-任务完成情况-杀死”
    @get_url(task_control_url)
    def test_a104_taskControl_completion_detail_kill(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_monitor_yaml/task_control_yaml/任务监控-任务完成情况-杀死.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = TaskControlPage(app)
        page.operate()
        page.check_point()

    # 校验“任务监控-任务完成情况-未知”
    @get_url(task_control_url)
    def test_a105_taskControl_completion_detail_unknown(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_monitor_yaml/task_control_yaml/任务监控-任务完成情况-未知.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = TaskControlPage(app)
        page.operate()
        page.check_point()

    # 校验“任务调度-详情列表-计划”
    @get_url(task_control_url)
    def test_a106_taskScheduler_detailList_plan(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_monitor_yaml/task_control_yaml/任务调度-详情列表-计划.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = TaskControlPage(app)
        page.operate()
        page.check_point()

    # 校验“任务调度-详情列表-计划-创建”
    @get_url(task_control_url)
    def test_a107_taskScheduler_detailList_plan_create(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_monitor_yaml/task_control_yaml/任务调度-详情列表-计划-创建.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = TaskControlPage(app)
        page.operate()
        page.check_point()

    # 校验“任务调度-详情列表-计划-停止”
    @get_url(task_control_url)
    def test_a108_taskScheduler_detailList_plan_stop(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_monitor_yaml/task_control_yaml/任务调度-详情列表-计划-停止.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = TaskControlPage(app)
        page.operate()
        page.check_point()

    # 校验“任务调度-详情列表-计划-启动”
    @get_url(task_control_url)
    def test_a109_taskScheduler_detailList_plan_start(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_monitor_yaml/task_control_yaml/任务调度-详情列表-计划-启动.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = TaskControlPage(app)
        page.operate()
        page.check_point()

    # 校验“任务调度-详情列表-计划-删除”
    @get_url(task_control_url)
    def test_a110_taskScheduler_detailList_plan_delete(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_monitor_yaml/task_control_yaml/任务调度-详情列表-计划-删除.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = TaskControlPage(app)
        page.operate()
        page.check_point()

    # 校验“任务调度-详情列表-执行”
    @get_url(task_control_url)
    def test_a111_taskScheduler_detailList_execute(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_monitor_yaml/task_control_yaml/任务调度-详情列表-执行.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = TaskControlPage(app)
        page.operate()
        page.check_point()

    # 校验“任务调度-详情列表-执行-重启”
    @get_url(task_control_url)
    def test_a112_taskScheduler_detailList_execute_rerun(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_monitor_yaml/task_control_yaml/任务调度-详情列表-执行-重启.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = TaskControlPage(app)
        page.operate()
        page.check_point()

    # 校验“任务调度-详情列表-执行-停止”
    @get_url(task_control_url)
    def test_a113_taskScheduler_detailList_execute_stop(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_monitor_yaml/task_control_yaml/任务调度-详情列表-执行-停止.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = TaskControlPage(app)
        page.operate()
        page.check_point()

    # 校验“任务调度-详情列表-执行-删除”
    @get_url(task_control_url)
    def test_a114_taskScheduler_detailList_execute_delete(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_monitor_yaml/task_control_yaml/任务调度-详情列表-执行-删除.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = TaskControlPage(app)
        page.operate()
        page.check_point()

    # 校验“任务调度-详细分析”
    @get_url(task_control_url)
    def test_a115_taskScheduler_detail_analyze(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_monitor_yaml/task_control_yaml/任务调度-详细分析.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = TaskControlPage(app)
        page.operate()
        page.check_point()

    # 校验“任务调度-悬停-任务调度”
    @get_url()
    def test_a116_taskScheduler(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_monitor_yaml/task_control_yaml/任务调度-悬停-任务调度.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = TaskControlPage(app)
        page.operate()
        page.check_point()

    # 校验“任务警告-详情列表-告警信息”
    @get_url(task_control_url)
    def test_a117_taskWarning_detail_warning_info(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_monitor_yaml/task_control_yaml/任务警告-详情列表-告警信息.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = TaskControlPage(app)
        page.operate()
        page.check_point()

    # 校验“任务警告-详情列表-告警规则”
    @get_url(task_control_url)
    def test_a118_taskWarning_detail_warning_rule(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_monitor_yaml/task_control_yaml/任务警告-详情列表-告警规则.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = TaskControlPage(app)
        page.operate()
        page.check_point()

    # 校验“任务警告-详情列表-告警规则-创建”
    @get_url(task_control_url)
    def test_a119_taskWarning_detail_warning_rule_create(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_monitor_yaml/task_control_yaml/任务警告-详情列表-告警规则-创建.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = TaskControlPage(app)
        page.operate()
        page.check_point()

    # 校验“任务警告-详情列表-告警规则-删除”
    @get_url(task_control_url)
    def test_a120_taskWarning_detail_warning_rule_delete(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_monitor_yaml/task_control_yaml/任务警告-详情列表-告警规则-删除.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = TaskControlPage(app)
        page.operate()
        page.check_point()

    @classmethod
    def setUpClass(cls):
        super(TaskControlTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TaskControlTest, cls).tearDownClass()




############# -----------------------------------=====================调试区=============================----------------------------------------------------------------------

# 任务监控页面测试
class TaskControlTest_SSSS(ParametrizedTestCase):
    task_control_url = ElementParam.TASK_CONTROL_URL

    def login(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/user_for_test/user_dir1.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = LoginTestPage(app)
        page.operate()

    def to_resource_dir(self):
        self.login()
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/任务监控.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = HomePage(app)
        page.operate()

    #链接到某url装饰器
    def get_url(to_url):
        def decorator(func):
            def wrapper(self, *args, **kwargs):
                self.driver.get(to_url)
                # self.driver.implicitly_wait(8)
                func(self, *args, **kwargs)
            return wrapper
        return decorator

    # 校验“任务监控-任务完成情况-详情”
    def test_a095_taskControl_completion_detail(self):
        self.to_resource_dir()

     # 校验“任务调度-详情列表-计划-创建”
    @get_url(task_control_url)
    def test_a107_taskScheduler_detailList_plan_create(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_monitor_yaml/task_control_yaml/任务调度-详情列表-计划-创建.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = TaskControlPage(app)
        page.operate()
        page.check_point()

    # 校验“任务调度-详情列表-计划-停止”
    @get_url(task_control_url)
    def test_a108_taskScheduler_detailList_plan_stop(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_monitor_yaml/task_control_yaml/任务调度-详情列表-计划-停止.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = TaskControlPage(app)
        page.operate()
        page.check_point()

    @classmethod
    def setUpClass(cls):
        super(TaskControlTest_SSSS, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TaskControlTest_SSSS, cls).tearDownClass()