# -*- coding: utf-8 -*-

from PageObject.data_analyze_page.project_dir_page.project_dir_page import ProjectDirPage
from common.BaseRunner import ParametrizedTestCase
from common.ElementParam import ElementParam
from PageObject.login.login_page import LoginTestPage
from PageObject.home.home_page import HomePage
import sys, os, time
from common.case_false_rerun import rerun
from common.login_who import who_login
from common.OperateFile import remove_path_key_file

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), p)
)

# 项目目录页面测试
class ProjectDirTest(ParametrizedTestCase):
    '''
    flow_management_url = ElementParam.FLOW_MANAGEMENT_URL
    project_dir_url = ElementParam.HOST + "/#/resourceManProject"
    workflow_plan_url = ElementParam.HOST + "/#/design/plan/84a1f206-1a0c-4e26-93c0-8606548b3309?type=workflow"
    '''
    project_dir_url = ElementParam.HOST + "/#/resourceManProject"
    project_dir_dataflow_plan_url = ElementParam.HOST + "/#/project/design/plan/c35f48e7-6c51-4fba-969e-294f43755a6d?type=dataflow"
    project_dir_workflow_plan_url = ElementParam.HOST + "/#/project/design/plan/4dc7fed8-be31-4ba5-8a13-ecdcb81c396a?type=workflow"


    def login(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH(who_login(self.who)),
               "caseName": sys._getframe().f_code.co_name}
        page = LoginTestPage(app)
        page.operate()

    def to_project_dir(self):
        self.login()
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/项目目录.yaml"),
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

    # 校验“项目目录-新建项目”
    @get_url()
    def test_a241_project_dir_create_project(self):
        self.to_project_dir()
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-新建项目.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-项目改名”
    @get_url()
    def test_a242_project_dir_rename_project(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-项目改名.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-项目删除”
    @get_url()
    def test_a243_project_dir_delete_project(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-项目删除.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-无数据-数据集列表”
    @get_url()
    def test_a244_project_dir_datasets_nodata(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-无数据-数据集列表.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-无数据-元数据列表”
    @get_url()
    def test_a245_project_dir_schemas_nodata(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-无数据-元数据列表.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-无数据-Flows列表”
    @get_url()
    def test_a246_project_dir_flows_nodata(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-无数据-Flows列表.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-数据集-新建hdfs数据集”
    @get_url()
    def test_a247_project_dir_datasets_create_hdfs(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-数据集-新建hdfs数据集.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-数据集-hdfs刷新获取数据”
    @get_url(project_dir_url)
    def test_a248_project_dir_datasets_hdfs_refresh_data(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-数据集-hdfs刷新获取数据.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-数据集-查看元数据”
    @get_url(project_dir_url)
    def test_a249_project_dir_datasets_view_schema(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-数据集-查看元数据.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-数据集-预览”
    @get_url(project_dir_url)
    def test_a250_project_dir_datasets_preview(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-数据集-预览.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-元数据-新建”
    @get_url(project_dir_url)
    def test_a251_project_dir_schema_schema(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-元数据-新建.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-元数据-复制”
    @get_url(project_dir_url)
    def test_a252_project_dir_schema_copy(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-元数据-复制.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-元数据-删除”
    @get_url(project_dir_url)
    def test_a253_project_dir_schema_delete(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-元数据-删除.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-flow-新建dataflow”
    @get_url(project_dir_url)
    def test_a254_project_dir_flow_create_dataflow(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-flow-新建dataflow.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-flow-新建workflow”
    @get_url(project_dir_url)
    def test_a255_project_dir_flow_create_workflow(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-flow-新建workflow.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-flow-新建制作json”
   # @get_url(project_dir_url)
   # def test_a256_project_dir_flow_create_json(self):
       # app = {"logTest": self.logTest, "driver": self.driver,
           #    "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-flow-新建制作json.yaml"),
           #    "caseName": sys._getframe().f_code.co_name}
      #  page = ProjectDirPage(app)
     #   page.operate()
      #  page.check_point()

    # 校验“项目目录-flow-导入”
    @get_url(project_dir_url)
    def test_a257_project_dir_flow_import(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-flow-导入.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-flow-导入后删除”
    @get_url(project_dir_url)
    def test_a258_project_dir_flow_delete(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-flow-导入后删除.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-flow-复制”
    @get_url(project_dir_url)
    def test_a259_project_dirt_flow_copy(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-flow-复制.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-flow-重命名”
    @get_url(project_dir_url)
    def test_a260_project_dir_flow_rename(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-flow-重命名.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-flow-导出”
    @get_url(project_dir_url)
    def test_a261_project_dir_flow_export(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-flow-导出.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()
        #删除指定路径下指定包含名称的所有文件
        print('重置数据：删除已经下载的文件')
        remove_path_key_file('dir1','C:\\Users\\Administrator\\Downloads')

    # 校验“项目目录-flow-删除”
    @get_url(project_dir_url)
    def test_a262_project_dir_flow_delete(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-flow-删除.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-flow-页面查看”
    @get_url(project_dir_url)
    def test_a263_project_dir_flow_view(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-flow-页面查看.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-flow-列表-计划查看”
    @get_url(project_dir_url)
    def test_a264_project_dir_flow_plan(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-flow-列表-计划查看.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-flow-列表-执行历史查看”
    @get_url(project_dir_url)
    def test_a265_project_dir_flow_history(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-flow-列表-执行历史查看.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-flow-dataflow-拖拽step”
    @get_url(project_dir_url)
    def test_a266_project_dir_flow_step_drag(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-flow-dataflow-拖拽step.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-flow-dataflow-保存”
    @get_url(project_dir_url)
    def test_a267_project_dir_flow_step_save(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-flow-dataflow-保存.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-flow-dataflow-step-重置”
    @get_url(project_dir_url)
    def test_a268_project_dir_flow_step_reset(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-flow-dataflow-step-重置.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-flow-dataflow-step-清空”
    @get_url(project_dir_url)
    def test_a269_project_dir_flow_step_clear(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-flow-dataflow-step-清空.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-flow-dataflow-step-返回”
    @get_url(project_dir_url)
    def test_a270_project_dir_flow_step_back(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-flow-dataflow-step-返回.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-flow-dataflow-step-历史”
    @get_url(project_dir_url)
    def test_a271_project_dir_flow_step_history(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-flow-dataflow-step-历史.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()
  #  ========================================= project_dataflow提交 start ========================================================================================
    # 校验“项目目录-dataflow-step-提交”
    @get_url(project_dir_url)
    def test_a272_project_dir_dataflow_submit(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-dataflow-step-提交.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-dataflow-step-计划”
    def test_a273_project_dir_dataflow_plan(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-dataflow-step-计划.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-dataflow-step-执行明细-running详细信息”
    def test_a274_project_dir_dataflow_detail_info_running(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-dataflow-step-执行明细-running详细信息.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-dataflow-step-执行明细-running输出”
    def test_a275_project_dir_dataflow_export_running(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-dataflow-step-执行明细-running输出.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-dataflow-step-执行明细-running日志”
    def test_a276_project_dir_dataflow_log_running(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-dataflow-step-执行明细-running日志.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

        # 校验“项目目录-dataflow-step-执行历史”
    def test_a277_project_dir_dataflow_history(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-dataflow-step-执行历史.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-dataflow-step-执行明细-success详细信息”
    def test_a278_project_dir_dataflow_detail_info_success(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-dataflow-step-执行明细-success详细信息.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-dataflow-step-执行明细-success输出”
    def test_a279_project_dir_dataflow_export_success(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-dataflow-step-执行明细-success输出.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-dataflow-step-执行明细-success输出-预览”
    def test_a280_project_dir_dataflow_export_success_preview(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-dataflow-step-执行明细-success输出-预览.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-dataflow-step-执行明细-success日志”
    def test_a281_project_dir_dataflow_log_success(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-dataflow-step-执行明细-success日志.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

# ========================================= project_dataflow 提交 end ========================================================================================
# +++++++++++++++++++++++++++++++++++++++++++++*************************************************************************++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ========================================= project_dataflow调度 start ========================================================================================

    # 校验“项目目录-dataflow-step-调度”
    @get_url(project_dir_url)
    def test_a282_project_dir_dataflow_schedule(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-dataflow-step-调度.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-dataflow-step-计划-调度”
    #@get_url( project_dir_dataflow_plan_url)
    def test_a283_project_dir_dataflow_plan_schedule(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-dataflow-step-计划-调度.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-dataflow-step-执行明细-running详细信息-schedule”
    def test_a284_project_dir_dataflow_step_detail_info_running_schedule(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-dataflow-step-执行明细-running详细信息-schedule.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-dataflow-step-执行明细-running输出-schedule”
    def test_a285_project_dir_dataflow_step_export_running_schedule(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-dataflow-step-执行明细-running输出-schedule.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-dataflow-step-执行明细-running日志-schedule”
    def test_a286_project_dir_dataflow_step_log_running_schedule(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-dataflow-step-执行明细-running日志-schedule.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-dataflow-step-执行历史-schedule”
    def test_a287_project_dir_dataflow_step_history_schedule(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-dataflow-step-执行历史-schedule.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()


        # 校验“项目目录-dataflow-step-执行明细-success详细信息-schedule”
    def test_a288_project_dir_dataflow_detail_info_success_schedule(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-dataflow-step-执行明细-success详细信息-schedule.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-dataflow-step-执行明细-success输出-schedule”
    def test_a289_project_dir_dataflow_export_success_schedule(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-dataflow-step-执行明细-success输出-schedule.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-dataflow-step-执行明细-success输出-预览-schedule”
    def test_a290_project_dir_dataflow_export_success_preview_schedule(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-dataflow-step-执行明细-success输出-预览-schedule.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-dataflow-step-执行明细-success日志-schedule”
    def test_a291_project_dir_dataflow_log_success_schedule(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-dataflow-step-执行明细-success日志-schedule.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()
#  ========================================= 项目目录--调度 end ========================================================================================

    # 校验“项目目录-dataflow-计划-点击名称”
    @get_url(project_dir_dataflow_plan_url)
    def test_a292_project_dir_dataflow_plan_click_name(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-dataflow-计划-点击名称.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-dataflow-计划-点击流程名称”
    @get_url(project_dir_dataflow_plan_url)
    def test_a293_project_dir_dataflow_plan_click_flowname(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-dataflow-计划-点击流程名称.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-dataflow-计划-停止”
    @get_url(project_dir_dataflow_plan_url)
    def test_a294_project_dir_dataflow_plan_stop(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-dataflow-计划-停止.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-dataflow-计划-启用”
    @get_url(project_dir_dataflow_plan_url)
    def test_a295_project_dir_dataflow_plan_start(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-dataflow-计划-启用.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-dataflow-计划-删除”
    @get_url(project_dir_dataflow_plan_url)
    def test_a296_project_dir_dataflow_plan_delete(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-dataflow-计划-删除.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-dataflow-执行历史-删除”
    @get_url(project_dir_dataflow_plan_url)
    def test_a297_project_dir_dataflow_history_delete(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-dataflow-执行历史-删除.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()


  # ----------------***********----------------------    项目目录-- workflow        ----------------***********----------------------
    # 校验“项目目录-flow-dataflow-拖拽step”
    @get_url(project_dir_url)
    def test_a298_project_dir_workflow_step_drag(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-workflow-拖拽step.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-workflow-保存”
    @get_url(project_dir_url)
    def test_a299_project_dir_workflow_step_save(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-workflow-保存.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-workflow-step-重置”
    @get_url(project_dir_url)
    def test_a300_project_dir_workflow_step_reset(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-workflow-step-重置.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-workflow-step-清空”
    @get_url(project_dir_url)
    def test_a301_project_dir_workflow_step_clear(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-workflow-step-清空.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-workflow-step-返回”
    @get_url(project_dir_url)
    def test_a302_project_dir_workflow_step_back(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-workflow-step-返回.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-workflow-step-历史”
    @get_url(project_dir_url)
    def test_a303_project_dir_workflow_step_history(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-workflow-step-历史.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

 #=========================================项目目录--workflow提交 start ========================================================================================
    # 校验“项目目录-workflow-step-提交”
    @get_url(project_dir_url)
    def test_a304_project_dir_workflow_submit(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-workflow-step-提交.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-workflow-step-计划”
    def test_a305_project_dir_workflow_plan(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-workflow-step-计划.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-workflow-step-执行明细-running详细信息”
    def test_a306_project_dir_workflow_detail_info_running(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-workflow-step-执行明细-running详细信息.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-workflow-step-执行明细-running输出”
    def test_a307_project_dir_workflow_detail_output_running(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-workflow-step-执行明细-running输出.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-workflow-step-执行明细-running日志”
    def test_a308_project_dir_workflow_detail_log_running(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-workflow-step-执行明细-running日志.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-workflow-step执行历史”
    def test_a309_project_dir_workflow_step_history(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-workflow-step执行历史.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()


    # 校验“项目目录-workflow-step-执行明细-success详细信息”
    def test_a310_project_dir_workflow_detail_info_success(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-workflow-step-执行明细-success详细信息.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-workflow-step-执行明细-success输出”
    def test_a311_project_dir_workflow_detail_output_success(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-workflow-step-执行明细-success输出.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-workflow-step-执行明细-success日志”
    def test_a312_project_dir_workflow_detail_log_success(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-workflow-step-执行明细-success日志.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

# =========================================项目目录--workflow 提交 end ========================================================================================
# ========================================= 项目目录 --workflow调度 start ========================================================================================
    # 校验“项目目录-workflow-step-调度”
    @get_url(project_dir_url)
    def test_a313_project_dir_workflow_schedule(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-workflow-step-调度.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-workflow-step-计划-调度”
    @get_url(project_dir_workflow_plan_url)
    def test_a314_project_dir_workflow_plan_schedule(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-workflow-step-计划-调度.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-workflow-step-执行明细-running详细信息-schedule”
    def test_a315_project_dir_workflow_detail_info_running_schedule(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-workflow-step-执行明细-running详细信息-schedule.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-workflow-step-执行明细-running输出-schedule”
    def test_a316_project_dir_workflow_output_running_schedule(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-workflow-step-执行明细-running输出-schedule.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-workflow-step-执行明细-running日志-schedule”
    def test_a317_project_dir_workflow_log_running_schedule(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-workflow-step-执行明细-running日志-schedule.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()


#     # 校验“流程管理-workflow-step-执行历史-schedule”
#     def test_a231_flow_management_workflow_step_history_schedule(self):
#         app = {"logTest": self.logTest, "driver": self.driver,
#                "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-workflow-step-执行历史-schedule.yaml"),
#                "caseName": sys._getframe().f_code.co_name}
#         page = FlowManagementPage(app)
#         page.operate()
#         page.check_point()
#
#     # 校验“流程管理-workflow-step-执行明细-success详细信息-schedule”
#     def test_a232_flow_management_workflow_step_detail_info_success_schedule(self):
#         app = {"logTest": self.logTest, "driver": self.driver,
#                "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-workflow-step-执行明细-success详细信息-schedule.yaml"),
#                "caseName": sys._getframe().f_code.co_name}
#         page = FlowManagementPage(app)
#         page.operate()
#         page.check_point()
#
#     # 校验“流程管理-workflow-step-执行明细-success输出-schedule”
#     def test_a233_flow_management_workflow_step_detail_output_success_schedule(self):
#         app = {"logTest": self.logTest, "driver": self.driver,
#                "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-workflow-step-执行明细-success输出-schedule.yaml"),
#                "caseName": sys._getframe().f_code.co_name}
#         page = FlowManagementPage(app)
#         page.operate()
#         page.check_point()
#
#     # 校验“流程管理-workflow-step-执行明细-success日志-schedule”
#     def test_a234_flow_management_workflow_step_detail_log_success_schedule(self):
#         app = {"logTest": self.logTest, "driver": self.driver,
#                "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-workflow-step-执行明细-success日志-schedule.yaml"),
#                "caseName": sys._getframe().f_code.co_name}
#         page = FlowManagementPage(app)
#         page.operate()
#         page.check_point()
# # ========================================= 调度 end ========================================================================================
#
#     # 校验“流程管理-workflow-计划-点击名称”
#     @get_url(workflow_plan_url)
#     def test_a235_flow_management_workflow_plan_click_name(self):
#         app = {"logTest": self.logTest, "driver": self.driver,
#                "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-workflow-计划-点击名称.yaml"),
#                "caseName": sys._getframe().f_code.co_name}
#         page = FlowManagementPage(app)
#         page.operate()
#         page.check_point()
#
#     # 校验“流程管理-workflow-计划-点击流程名称”
#     @get_url(workflow_plan_url)
#     def test_a236_flow_management_workflow_plan_click_flowname(self):
#         app = {"logTest": self.logTest, "driver": self.driver,
#                "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-workflow-计划-点击流程名称.yaml"),
#                "caseName": sys._getframe().f_code.co_name}
#         page = FlowManagementPage(app)
#         page.operate()
#         page.check_point()
#
#     # 校验“流程管理-workflow-计划-停止”
#     @get_url(workflow_plan_url)
#     def test_a237_workflow_management_plan_stop(self):
#         app = {"logTest": self.logTest, "driver": self.driver,
#                "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-workflow-计划-停止.yaml"),
#                "caseName": sys._getframe().f_code.co_name}
#         page = FlowManagementPage(app)
#         page.operate()
#         page.check_point()
#
#     # 校验“流程管理-workflow-计划-启用”
#     @get_url(workflow_plan_url)
#     def test_a238_flow_management_workflow_plan_start(self):
#         app = {"logTest": self.logTest, "driver": self.driver,
#                "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-workflow-计划-启动.yaml"),
#                "caseName": sys._getframe().f_code.co_name}
#         page = FlowManagementPage(app)
#         page.operate()
#         page.check_point()
#
#     # 校验“流程管理-workflow-计划-删除”
#     @get_url(workflow_plan_url)
#     def test_a239_flow_management_workflow_plan_delete(self):
#         app = {"logTest": self.logTest, "driver": self.driver,
#                "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-workflow-计划-删除.yaml"),
#                "caseName": sys._getframe().f_code.co_name}
#         page = FlowManagementPage(app)
#         page.operate()
#         page.check_point()
#
#     # 校验“流程管理-workflow-执行历史-删除”
#     @get_url(workflow_plan_url)
#     def test_a240_flow_management_workflow_history_delete(self):
#         app = {"logTest": self.logTest, "driver": self.driver,
#                "path": PATH("../YAML/data_analyze_yaml/flow_management_yaml/流程管理-workflow-执行历史-删除.yaml"),
#                "caseName": sys._getframe().f_code.co_name}
#         page = FlowManagementPage(app)
#         page.operate()
#         page.check_point()
#



    @classmethod
    def setUpClass(cls):
        super(ProjectDirTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(ProjectDirTest, cls).tearDownClass()




#### --------------------------------------=========================调试区====================================-------------------------------------------------------------


# 项目目录页面测试
class ProjectDirTest_SSSS(ParametrizedTestCase):
    '''
    flow_management_url = ElementParam.FLOW_MANAGEMENT_URL
    project_dir_url = ElementParam.HOST + "/#/resourceManProject"
    workflow_plan_url = ElementParam.HOST + "/#/design/plan/84a1f206-1a0c-4e26-93c0-8606548b3309?type=workflow"
    '''
    project_dir_url = ElementParam.HOST + "/#/resourceManProject"
    project_dir_dataflow_plan_url = ElementParam.HOST + "/#/project/design/plan/c35f48e7-6c51-4fba-969e-294f43755a6d?type=dataflow"
    project_dir_workflow_plan_url = ElementParam.HOST + "/#/project/design/plan/4dc7fed8-be31-4ba5-8a13-ecdcb81c396a?type=workflow"


    def login(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/user_for_test/user_dir1.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = LoginTestPage(app)
        page.operate()

    def to_project_dir(self):
        self.login()
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/项目目录.yaml"),
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

    # 校验“项目目录-新建项目”
    def test_a241_project_dir_create_project(self):
        self.to_project_dir()

    # 校验“项目目录-workflow-step-提交”
    @get_url(project_dir_url)
    def test_a304_project_dir_workflow_submit(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-workflow-step-提交.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-workflow-step-计划”
    def test_a305_project_dir_workflow_plan(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-workflow-step-计划.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-workflow-step-执行明细-running详细信息”
    def test_a306_project_dir_workflow_detail_info_running(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-workflow-step-执行明细-running详细信息.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-workflow-step-执行明细-running输出”
    def test_a307_project_dir_workflow_detail_output_running(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-workflow-step-执行明细-running输出.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-workflow-step-执行明细-running日志”
    def test_a308_project_dir_workflow_detail_log_running(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-workflow-step-执行明细-running日志.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-workflow-step执行历史”
    def test_a309_project_dir_workflow_step_history(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-workflow-step执行历史.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-workflow-step-执行明细-success详细信息”
    def test_a310_project_dir_workflow_detail_info_success(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-workflow-step-执行明细-success详细信息.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-workflow-step-执行明细-success输出”
    def test_a311_project_dir_workflow_detail_output_success(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-workflow-step-执行明细-success输出.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    # 校验“项目目录-workflow-step-执行明细-success日志”
    def test_a312_project_dir_workflow_detail_log_success(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_analyze_yaml/project_dir_yaml/项目目录-workflow-step-执行明细-success日志.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ProjectDirPage(app)
        page.operate()
        page.check_point()

    @classmethod
    def setUpClass(cls):
        super(ProjectDirTest_SSSS, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(ProjectDirTest_SSSS, cls).tearDownClass()
