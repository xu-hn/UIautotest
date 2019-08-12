# -*- coding: utf-8 -*-

from PageObject.data_analyze_page.flow_management_page.flow_management_page import FlowManagementPage
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

# 流程管理页面测试
class FlowManagementTest(ParametrizedTestCase):
    flow_management_url = ElementParam.FLOW_MANAGEMENT_URL
    flow_plan_url = ElementParam.HOST + "/#/design/plan/d1942b2c-c78b-479c-9a75-65561b3381bf?type=dataflow"
    workflow_plan_url = ElementParam.HOST + "/#/design/plan/698098e2-73ec-4f0b-9f43-54043e8cbaae?type=workflow"


    def login(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH(who_login(self.who)),
               "caseName": sys._getframe().f_code.co_name}
        page = LoginTestPage(app)
        page.operate()

    def to_resource_dir(self):
        self.login()
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/流程管理.yaml"),
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

    # 校验“流程管理-新建-dataflow”
    @get_url()
    def test_a167_flow_management_create_dataflow(self):
        self.to_resource_dir()
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-新建-dataflow.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-新建-workflow”
    @get_url()
    def test_a168_flow_management_create_workflow(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-新建-workflow.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-新建-streamflow”
    @get_url()
    def test_a169_flow_management_create_streamflow(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-新建-streamflow.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-flow-重命名”
    @get_url()
    def test_a170_flow_management_flow_rename(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-flow-重命名.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-flow-复制”
    @get_url()
    def test_a171_flow_management_flow_copy(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-flow-复制.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-flow-移动”
    @get_url()
    def test_a172_flow_management_flow_move(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-flow-移动.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-flow-删除”
    @get_url()
    def test_a173_flow_management_flow_delete(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-flow-删除.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-flow-页面查看”
    @get_url()
    def test_a174_flow_management_flow_view(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-flow-页面查看.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-flow-列表-计划查看”
    @get_url(flow_management_url)
    def test_a175_flow_management_flow_plan(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-flow-列表-计划查看.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-flow-列表-执行历史查看”
    @get_url(flow_management_url)
    def test_a176_flow_management_flow_history(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-flow-列表-执行历史查看.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-flow-列表-制作json”
    @get_url(flow_management_url)
    def test_a177_flow_management_flow_make_json(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-flow-列表-制作json.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-flow-导出”
    @get_url(flow_management_url)
    def test_a178_flow_management_flow_import(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-flow-导出.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-flow-拖拽step”
    @get_url(flow_management_url)
    def test_a178_flow_management_flow_step_drag(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-flow-拖拽step.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-flow-step-保存”
    @get_url(flow_management_url)
    def test_a179_flow_management_flow_step_save(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-flow-step-保存.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-flow-step-重置”
    @get_url(flow_management_url)
    def test_a180_flow_management_flow_step_reset(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-flow-step-重置.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-flow-step-清空”
    @get_url(flow_management_url)
    def test_a181_flow_management_flow_step_clear(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-flow-step-清空.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-flow-step-返回”
    @get_url(flow_management_url)
    def test_a182_flow_management_flow_step_back(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-flow-step-返回.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-flow-step-历史”
    @get_url(flow_management_url)
    def test_a183_flow_management_flow_step_history(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-flow-step-历史.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()
#  ========================================= 提交 start ========================================================================================
    # 校验“流程管理-flow-step-提交”
    @get_url(flow_management_url)
    def test_a184_flow_management_flow_step_submit(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-flow-step-提交.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-flow-step-计划”
    def test_a185_flow_management_flow_step_plan(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-flow-step-计划.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-flow-step-执行明细-running详细信息”
    def test_a186_flow_management_flow_step_detail_info_running(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-flow-step-执行明细-running详细信息.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-flow-step-执行明细-running输出”
    def test_a187_flow_management_flow_step_detail_output_running(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-flow-step-执行明细-running输出.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-flow-step-执行明细-running日志”
    def test_a188_flow_management_flow_step_detail_log_running(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-flow-step-执行明细-running日志.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-flow-step-执行历史”
    def test_a189_flow_management_flow_step_history(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-flow-step-执行历史.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-flow-step-执行明细-success详细信息”
    def test_a190_flow_management_flow_step_detail_info_success(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-flow-step-执行明细-success详细信息.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-flow-step-执行明细-success输出”
    def test_a191_flow_management_flow_step_detail_output_success(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-flow-step-执行明细-success输出.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-flow-step-执行明细-success输出-预览”
    def test_a192_flow_management_flow_step_detail_output_success_preview(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-flow-step-执行明细-success输出-预览.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-flow-step-执行明细-success日志”
    def test_a193_flow_management_flow_step_detail_log_success(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-flow-step-执行明细-success日志.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()
# ========================================= 提交 end ========================================================================================
# ========================================= 调度 start ========================================================================================

    # 校验“流程管理-flow-step-调度”
    @get_url(flow_management_url)
    def test_a195_flow_management_flow_step_schedule(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-flow-step-调度.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-flow-step-计划-调度”
    @get_url(flow_plan_url)
    def test_a196_flow_management_flow_step_plan_schedule(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-flow-step-计划-调度.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-flow-step-执行明细-running详细信息-schedule”
    def test_a197_flow_management_flow_step_detail_info_running_schedule(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-flow-step-执行明细-running详细信息-schedule.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-flow-step-执行明细-running输出-schedule”
    def test_a198_flow_management_flow_step_detail_output_running_schedule(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-flow-step-执行明细-running输出-schedule.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-flow-step-执行明细-running日志-schedule”
    def test_a199_flow_management_flow_step_detail_log_running_schedule(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-flow-step-执行明细-running日志-schedule.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-flow-step-执行历史-schedule”
    def test_a200_flow_management_flow_step_history_schedule(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-flow-step-执行历史-schedule.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-flow-step-执行明细-success详细信息-schedule”
    def test_a201_flow_management_flow_step_detail_info_success_schedule(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-flow-step-执行明细-success详细信息-schedule.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-flow-step-执行明细-success输出-schedule”
    def test_a202_flow_management_flow_step_detail_output_success_schedule(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-flow-step-执行明细-success输出-schedule.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-flow-step-执行明细-success输出-预览-schedule”
    def test_a203_flow_management_flow_step_detail_output_success_preview_schedule(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-flow-step-执行明细-success输出-预览-schedule.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-flow-step-执行明细-success日志-schedule”
    def test_a204_flow_management_flow_step_detail_log_success_schedule(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-flow-step-执行明细-success日志-schedule.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()
#  ========================================= 调度 end ========================================================================================

    # 校验“流程管理-flow-计划-点击名称”
    @get_url(flow_plan_url)
    def test_a205_flow_management_plan_click_name(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-flow-计划-点击名称.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-flow-计划-点击流程名称”
    @get_url(flow_plan_url)
    def test_a206_flow_management_plan_click_flowname(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-flow-计划-点击流程名称.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-flow-计划-停止”
    @get_url(flow_plan_url)
    def test_a207_flow_management_plan_stop(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-flow-计划-停止.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-flow-计划-启用”
    @get_url(flow_plan_url)
    def test_a208_flow_management_plan_start(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-flow-计划-启动.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-flow-计划-删除”
    @get_url(flow_plan_url)
    def test_a209_flow_management_plan_delete(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-flow-计划-删除.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-flow-执行历史-删除”
    @get_url(flow_plan_url)
    def test_a210_flow_management_history_delete(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-flow-执行历史-删除.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()


   # ----------------***********----------------------       workflow        ----------------***********----------------------

    # 校验“流程管理-workflow-拖拽step”
    @get_url(flow_management_url)
    def test_a211_flow_management_flow_step_drag(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-workflow-拖拽step.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-flow-workstep-保存”
    @get_url(flow_management_url)
    def test_a212_flow_management_workflow_step_save(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-workflow-step-保存.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-workflow-step-重置”
    @get_url(flow_management_url)
    def test_a213_workflow_management_workflow_step_reset(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-workflow-step-重置.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-workflow-step-清空”
    @get_url(flow_management_url)
    def test_a214_workflow_management_workflow_step_clear(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-workflow-step-清空.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-workflow-step-返回”
    @get_url(flow_management_url)
    def test_a215_workflow_management_flow_step_back(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-workflow-step-返回.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-workflow-step-历史”
    @get_url(flow_management_url)
    def test_a216_workflow_management_flow_step_history(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-workflow-step-历史.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()
#========================================= workflow提交 start ========================================================================================
    # 校验“流程管理-workflow-step-提交”
    @get_url(flow_management_url)
    def test_a217_flow_management_workflow_step_submit(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-workflow-step-提交.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-workflow-step-计划”
    def test_a218_flow_management_workflow_step_plan(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-workflow-step-计划.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-workflow-step-执行明细-running详细信息”
    def test_a219_flow_management_workflow_step_detail_info_running(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-workflow-step-执行明细-running详细信息.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-workflow-step-执行明细-running输出”
    def test_a220_flow_management_workflow_step_detail_output_running(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-workflow-step-执行明细-running输出.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-workflow-step-执行明细-running日志”
    def test_a221_flow_management_workflow_step_detail_log_running(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-workflow-step-执行明细-running日志.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-workflow-step-执行历史”
    def test_a222_flow_management_workflow_step_history(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-workflow-step-执行历史.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-workflow-step-执行明细-success详细信息”
    def test_a223_flow_management_workflow_step_detail_info_success(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-workflow-step-执行明细-success详细信息.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-workflow-step-执行明细-success输出”
    def test_a224_flow_management_workflow_step_detail_output_success(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-workflow-step-执行明细-success输出.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-workflow-step-执行明细-success日志”
    def test_a225_flow_management_workflow_step_detail_log_success(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-workflow-step-执行明细-success日志.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()
# =========================================workflow 提交 end ========================================================================================
# ========================================= workflow调度 start ========================================================================================

    # 校验“流程管理-workflow-step-调度”
    @get_url(flow_management_url)
    def test_a226_flow_management_workflow_step_schedule(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-workflow-step-调度.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-workflow-step-计划-调度”
    @get_url(workflow_plan_url)
    def test_a227_flow_management_workflow_step_plan_schedule(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-workflow-step-计划-调度.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-workflow-step-执行明细-running详细信息-schedule”
    def test_a228_flow_management_workflow_step_detail_info_running_schedule(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-workflow-step-执行明细-running详细信息-schedule.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-workflow-step-执行明细-running输出-schedule”
    def test_a229_flow_management_workflow_step_detail_output_running_schedule(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-workflow-step-执行明细-running输出-schedule.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-workflow-step-执行明细-running日志-schedule”
    def test_a230_flow_management_workflow_step_detail_log_running_schedule(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-workflow-step-执行明细-running日志-schedule.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-workflow-step-执行历史-schedule”
    def test_a231_flow_management_workflow_step_history_schedule(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-workflow-step-执行历史-schedule.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-workflow-step-执行明细-success详细信息-schedule”
    def test_a232_flow_management_workflow_step_detail_info_success_schedule(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-workflow-step-执行明细-success详细信息-schedule.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-workflow-step-执行明细-success输出-schedule”
    def test_a233_flow_management_workflow_step_detail_output_success_schedule(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-workflow-step-执行明细-success输出-schedule.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-workflow-step-执行明细-success日志-schedule”
    def test_a234_flow_management_workflow_step_detail_log_success_schedule(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-workflow-step-执行明细-success日志-schedule.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()
# ========================================= 调度 end ========================================================================================

    # 校验“流程管理-workflow-计划-点击名称”
    @get_url(workflow_plan_url)
    def test_a235_flow_management_workflow_plan_click_name(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-workflow-计划-点击名称.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-workflow-计划-点击流程名称”
    @get_url(workflow_plan_url)
    def test_a236_flow_management_workflow_plan_click_flowname(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-workflow-计划-点击流程名称.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-workflow-计划-停止”
    @get_url(workflow_plan_url)
    def test_a237_workflow_management_plan_stop(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-workflow-计划-停止.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-workflow-计划-启用”
    @get_url(workflow_plan_url)
    def test_a238_flow_management_workflow_plan_start(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-workflow-计划-启动.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-workflow-计划-删除”
    @get_url(workflow_plan_url)
    def test_a239_flow_management_workflow_plan_delete(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-workflow-计划-删除.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-workflow-执行历史-删除”
    @get_url(workflow_plan_url)
    def test_a240_flow_management_workflow_history_delete(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-workflow-执行历史-删除.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()


     #  ========================================= mysql_to_hive_flow提交 start ========================================================================================
    # 校验“流程管理-mysql_to_hive_flow-step-提交”
    @get_url(flow_management_url)
    def test_c001_mysql_to_hive_flow_management_flow_step_submit(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-mysql_to_hive-flow-step-提交.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-mysql_to_hive-flow-step-计划.yaml”
    def test_c002_mysql_to_hive_flow_management_flow_step_plan(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-mysql_to_hive-flow-step-计划.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理mysql_to_hive_-flow-step-执行明细-running详细信息”
    def test_c003_mysql_to_hive_flow_management_flow_step_detail_info_running(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-mysql_to_hive-flow-step-执行明细-running详细信息.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-mysql_to_hive_-flow-step-执行明细-running输出”
    def test_c004_mysql_to_hive_flow_management_flow_step_detail_output_running(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-mysql_to_hive-flow-step-执行明细-running输出.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理_mysql_to_hive-flow-step-执行明细-running日志”
    def test_c005_mysql_to_hive_flow_flow_management_flow_step_detail_log_running(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-mysql_to_hive-flow-step-执行明细-running日志.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理_mysql_to_hive-flow-step-执行历史”
    def test_c006_mysql_to_hive_flow_management_flow_step_history(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-mysql_to_hive-flow-step-执行历史.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-mysql_to_hive-flow-step-执行明细-success详细信息”
    def test_c007_mysql_to_hive_flow_management_flow_step_detail_info_success(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-mysql_to_hive-flow-step-执行明细-success详细信息.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-mysql_to_hive-flow-step-执行明细-success输出”
    def test_c008_mysql_to_hive_flow_management_flow_step_detail_output_success(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-mysql_to_hive-flow-step-执行明细-success输出.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-mysql_to_hive-flow-step-执行明细-success输出-预览”
    def test_c009_mysql_to_hive_flow_management_flow_step_detail_output_success_preview(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-mysql_to_hive-flow-step-执行明细-success输出-预览.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-mysql_to_hive-flow-step-执行明细-success日志”
    def test_c010_mysql_to_hive_flow_management_flow_step_detail_log_success(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-mysql_to_hive-flow-step-执行明细-success日志.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()
# ========================================= 提交 end ========================================================================================


    @classmethod
    def setUpClass(cls):
        super(FlowManagementTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(FlowManagementTest, cls).tearDownClass()



# -----------------------------------------------------------===========================调试区====================================-----------------------------------------------------------

# 流程管理页面测试
class FlowManagementTest_SSSS(ParametrizedTestCase):
    flow_management_url = ElementParam.FLOW_MANAGEMENT_URL
    flow_plan_url = ElementParam.HOST + "/#/design/plan/d1942b2c-c78b-479c-9a75-65561b3381bf?type=dataflow"
    # flow_plan_url = ElementParam.HOST + "/#/design/plan/36a372dd-4449-45a8-8c57-6e79cf2f96f7?type=dataflow"
    # workflow_plan_url = ElementParam.HOST + "/#/design/plan/84a1f206-1a0c-4e26-93c0-8606548b3309?type=workflow"
    workflow_plan_url = ElementParam.HOST + "/#/design/plan/698098e2-73ec-4f0b-9f43-54043e8cbaae?type=workflow"


    def login(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/user_for_test/user_dir1.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = LoginTestPage(app)
        page.operate()

    def to_resource_dir(self):
        self.login()
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/流程管理.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = HomePage(app)
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

    # 校验“流程管理-新建-dataflow”
    def test_a167_flow_management_create_dataflow(self):
        self.to_resource_dir()

    #  ========================================= 提交 start ========================================================================================
    # 校验“流程管理-flow-step-提交”
    @get_url(flow_management_url)
    def test_a184_flow_management_flow_step_submit(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-flow-step-提交.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-flow-step-计划”
    def test_a185_flow_management_flow_step_plan(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-flow-step-计划.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-flow-step-执行明细-running详细信息”
    def test_a186_flow_management_flow_step_detail_info_running(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-flow-step-执行明细-running详细信息.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-flow-step-执行明细-running输出”
    def test_a187_flow_management_flow_step_detail_output_running(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-flow-step-执行明细-running输出.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-flow-step-执行明细-running日志”
    def test_a188_flow_management_flow_step_detail_log_running(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-flow-step-执行明细-running日志.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-flow-step-执行历史”
    def test_a189_flow_management_flow_step_history(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-flow-step-执行历史.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-flow-step-执行明细-success详细信息”
    def test_a190_flow_management_flow_step_detail_info_success(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-flow-step-执行明细-success详细信息.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-flow-step-执行明细-success输出”
    def test_a191_flow_management_flow_step_detail_output_success(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-flow-step-执行明细-success输出.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-flow-step-执行明细-success输出-预览”
    def test_a192_flow_management_flow_step_detail_output_success_preview(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-flow-step-执行明细-success输出-预览.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“流程管理-flow-step-执行明细-success日志”
    def test_a193_flow_management_flow_step_detail_log_success(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-flow-step-执行明细-success日志.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = FlowManagementPage(app)
        page.operate()
        page.check_point()
# ========================================= 提交 end ========================================================================================


    @classmethod
    def setUpClass(cls):
        super(FlowManagementTest_SSSS, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(FlowManagementTest_SSSS, cls).tearDownClass()

