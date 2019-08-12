# -*- coding: utf-8 -*-

from PageObject.data_govern_page.quality_analyze_page.quality_analyza_page import QualityAnalyzaPage
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

# 质量分析页面测试
class QualityAnalyzeTest(ParametrizedTestCase):
    execute_info_url = ElementParam.EXECUTE_INFO_URL
    analysis_template_url = ElementParam.ANALYZE_TEMPLATE_URL
    analyze_rules_url = ElementParam.ANALYZE_RULES_URL
    er_statistics_url = ElementParam.ER_STATISTICS_URL

    def login(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH(who_login(self.who)),
               "caseName": sys._getframe().f_code.co_name}
        page = LoginTestPage(app)
        page.operate()

    def to_resource_dir(self):
        self.login()
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/质量分析.yaml"),
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

    # 校验“质量分析-分析模板-运行”
    @get_url()
    def test_a121_qualityanalyze_mode_run(self):
        self.to_resource_dir()
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_govern_yaml/quality_analyze_yaml/质量分析-分析模板-运行.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = QualityAnalyzaPage(app)
        page.operate()
        page.check_point()

    # 校验“质量分析-任务执行信息-查看模板信息”
    @get_url(execute_info_url)
    def test_a122_qualityanalyze_taskeexecuteinfo_modeinfo(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_govern_yaml/quality_analyze_yaml/质量分析-任务执行信息-查看模板信息.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = QualityAnalyzaPage(app)
        page.operate()
        page.check_point()


    # 校验“质量分析-任务执行信息-查看模板信息-返回”
    @get_url()
    def test_a123_qualityanalyze_taskeexecuteinfo_modeinfo_back(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_govern_yaml/quality_analyze_yaml/质量分析-任务执行信息-查看模板信息-返回.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = QualityAnalyzaPage(app)
        page.operate()
        page.check_point()

    # 校验“质量分析-任务执行信息-查看任务信息”
    @get_url(execute_info_url)
    def test_a124_qualityanalyze_taskeexecuteinfo_taskinfo(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_govern_yaml/quality_analyze_yaml/质量分析-任务执行信息-查看任务信息.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = QualityAnalyzaPage(app)
        page.operate()
        page.check_point()

    # 校验“质量分析-任务执行信息-查看任务信息-返回”
    @get_url(execute_info_url)
    def test_a125_qualityanalyze_taskeexecuteinfo_taskinfo_back(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_govern_yaml/quality_analyze_yaml/质量分析-任务执行信息-查看任务信息-返回.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = QualityAnalyzaPage(app)
        page.operate()
        page.check_point()

    # 校验“质量分析-任务执行信息-查看日志”
    @get_url(execute_info_url)
    def test_a126_qualityanalyze_taskeexecuteinfo_loginfo(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_govern_yaml/quality_analyze_yaml/质量分析-任务执行信息-查看日志.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = QualityAnalyzaPage(app)
        page.operate()
        page.check_point()

    # 校验“质量分析-任务执行信息-查看日志-关闭”
    @get_url(execute_info_url)
    def test_a127_qualityanalyze_taskeexecuteinfo_loginfo_close(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_govern_yaml/quality_analyze_yaml/质量分析-任务执行信息-查看日志-关闭.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = QualityAnalyzaPage(app)
        page.operate()
        page.check_point()

    # 校验“质量分析-任务执行信息-任务状态”
    @get_url(execute_info_url)
    def test_a128_qualityanalyze_taskeexecuteinfo_taskstatus(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_govern_yaml/quality_analyze_yaml/质量分析-任务执行信息-任务状态.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = QualityAnalyzaPage(app)
        page.operate()
        page.check_point()

    # 校验“质量分析-任务执行信息-进入结果”
    @get_url(execute_info_url)
    def test_a129_qualityanalyze_taskeexecuteinfo_result(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_govern_yaml/quality_analyze_yaml/质量分析-任务执行信息-结果.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = QualityAnalyzaPage(app)
        page.operate()
        page.check_point()

    #校验“质量分析-任务执行信息-进入结果-返回”
    @get_url(execute_info_url)
    def test_a130_qualityanalyze_taskeexecuteinfo_result_back(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_govern_yaml/quality_analyze_yaml/质量分析-任务执行信息-结果-返回.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = QualityAnalyzaPage(app)
        page.operate()
        page.check_point()

    # 校验“质量分析-任务执行信息-结果-模板规则”
    @get_url(execute_info_url)
    def test_a131_qualityanalyze_taskeexecuteinfo_result_mode_rule(self):

        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_govern_yaml/quality_analyze_yaml/质量分析-任务执行信息-结果-模板规则.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = QualityAnalyzaPage(app)
        page.operate()
        page.check_point()

    # 校验“质量分析-任务执行信息-结果-模板规则-返回”
    @get_url(execute_info_url)
    def test_a132_qualityanalyze_taskeexecuteinfo_result_mode_rule_back(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_govern_yaml/quality_analyze_yaml/质量分析-任务执行信息-结果-模板规则-返回.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = QualityAnalyzaPage(app)
        page.operate()
        page.check_point()

    # 校验“质量分析-任务执行信息-结果-模板规则-解锁”
    @get_url(execute_info_url)
    def test_a133_qualityanalyze_taskeexecuteinfo_result_mode_rule_unlock(self):

        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_govern_yaml/quality_analyze_yaml/质量分析-任务执行信息-结果-模板规则-解锁.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = QualityAnalyzaPage(app)
        page.operate()
        page.check_point()

    # 校验“质量分析-任务执行信息-结果-基准规则”
    @get_url(execute_info_url)
    def test_a134_qualityanalyze_taskeexecuteinfo_result_base_rule(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_govern_yaml/quality_analyze_yaml/质量分析-任务执行信息-结果-基准规则.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = QualityAnalyzaPage(app)
        page.operate()
        page.check_point()

    # 校验“质量分析-任务执行信息-结果-基准规则-返回”
    @get_url(execute_info_url)
    def test_a135_qualityanalyze_taskeexecuteinfo_result_base_rule_back(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_govern_yaml/quality_analyze_yaml/质量分析-任务执行信息-结果-基准规则-返回.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = QualityAnalyzaPage(app)
        page.operate()
        page.check_point()

    # 校验“质量分析-任务执行信息-结果-查看”
    @get_url(execute_info_url)
    def test_a136_qualityanalyze_taskeexecuteinfo_result_view(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_govern_yaml/quality_analyze_yaml/质量分析-任务执行信息-结果-查看.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = QualityAnalyzaPage(app)
        page.operate()
        page.check_point()

    # 校验“质量分析-任务执行信息-结果-查看-取消”
    @get_url(execute_info_url)
    def test_a137_qualityanalyze_taskeexecuteinfo_result_view_back(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_govern_yaml/quality_analyze_yaml/质量分析-任务执行信息-结果-查看-取消.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = QualityAnalyzaPage(app)
        page.operate()
        page.check_point()

    # 校验“质量分析-任务执行信息-结果-查看-下载”
    @get_url(execute_info_url)
    def test_a138_qualityanalyze_taskeexecuteinfo_result_download(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_govern_yaml/quality_analyze_yaml/质量分析-任务执行信息-结果-下载.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = QualityAnalyzaPage(app)
        page.operate()
        page.check_point()

    # 校验“质量分析-分析模板-新建”
    @get_url(analysis_template_url)
    def test_a139_qualityanalyze_analyzetemplate_create(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_govern_yaml/quality_analyze_yaml/质量分析-分析模板-新建.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = QualityAnalyzaPage(app)
        page.operate()
        page.check_point()

    # 校验“质量分析-分析模板-规则-新建”
    @get_url(analysis_template_url)
    def test_a140_qualityanalyze_analyzetemplate_rule_create(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_govern_yaml/quality_analyze_yaml/质量分析-分析模板-规则-新建.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = QualityAnalyzaPage(app)
        page.operate()
        page.check_point()

    # 校验“质量分析-分析模板-规则-运行”
    @get_url(analysis_template_url)
    def test_a141_qualityanalyze_analyzetemplate_rule_run(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_govern_yaml/quality_analyze_yaml/质量分析-分析模板-规则-运行.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = QualityAnalyzaPage(app)
        page.operate()
        page.check_point()

    # 校验“质量分析-分析模板-规则-周期”
    @get_url(analysis_template_url)
    def test_a142_qualityanalyze_analyzetemplate_rule_cycle(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_govern_yaml/quality_analyze_yaml/质量分析-分析模板-规则-周期.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = QualityAnalyzaPage(app)
        page.operate()
        page.check_point()

    # 校验“质量分析-分析模板-规则-查看”
    @get_url(analysis_template_url)
    def test_a143_qualityanalyze_analyzetemplate_rule_view(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_govern_yaml/quality_analyze_yaml/质量分析-分析模板-规则-查看.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = QualityAnalyzaPage(app)
        page.operate()
        page.check_point()

    # 校验“质量分析-分析模板-规则-返回”
    @get_url(analysis_template_url)
    def test_a144_qualityanalyze_analyzetemplate_rule_back(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_govern_yaml/quality_analyze_yaml/质量分析-分析模板-规则-返回.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = QualityAnalyzaPage(app)
        page.operate()
        page.check_point()

    # 校验“质量分析-分析模板-规则-停止”
    @get_url(analysis_template_url)
    def test_a145_qualityanalyze_analyzetemplate_rule_stop(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_govern_yaml/quality_analyze_yaml/质量分析-分析模板-规则-停止.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = QualityAnalyzaPage(app)
        page.operate()
        page.check_point()

    # 校验“质量分析-分析模板-规则-启用”
    @get_url(analysis_template_url)
    def test_a146_qualityanalyze_analyzetemplate_rule_starp(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_govern_yaml/quality_analyze_yaml/质量分析-分析模板-规则-启用.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = QualityAnalyzaPage(app)
        page.operate()
        page.check_point()

    # 校验“质量分析-分析模板-规则-删除”
    @get_url(analysis_template_url)
    def test_a147_qualityanalyze_analyzetemplate_rule_delete(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_govern_yaml/quality_analyze_yaml/质量分析-分析模板-规则-删除.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = QualityAnalyzaPage(app)
        page.operate()
        page.check_point()

    # 校验“质量分析-分析模板-启动周期任务”
    @get_url(analysis_template_url)
    def test_a148_qualityanalyze_analyzetemplate_cycle(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_govern_yaml/quality_analyze_yaml/质量分析-分析模板-启动周期任务.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = QualityAnalyzaPage(app)
        page.operate()
        page.check_point()

    # 校验“质量分析-分析模板-删除”
    @get_url(analysis_template_url)
    def test_a149_qualityanalyze_analyzetemplate_delete(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_govern_yaml/quality_analyze_yaml/质量分析-分析模板-删除.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = QualityAnalyzaPage(app)
        page.operate()
        page.check_point()

    # 校验“质量分析-分析模板-编辑规则”
    @get_url(analysis_template_url)
    def test_a150_qualityanalyze_analyzetemplate_edit_rule(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_govern_yaml/quality_analyze_yaml/质量分析-分析模板-进入编辑规则.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = QualityAnalyzaPage(app)
        page.operate()
        page.check_point()

    # 校验“质量分析-分析模板-任务页面”
    @get_url(analysis_template_url)
    def test_a151_qualityanalyze_analyzetemplate_task(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_govern_yaml/quality_analyze_yaml/质量分析-分析模板-任务页面.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = QualityAnalyzaPage(app)
        page.operate()
        page.check_point()

    # 校验“质量分析-分析模板-分析规则-新建-EL规则”
    @get_url(analyze_rules_url)
    def test_a152_qualityanalyze_analyzetemplate_analyzerule_create_el(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_govern_yaml/quality_analyze_yaml/质量分析-分析模板-分析规则-新建-EL规则.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = QualityAnalyzaPage(app)
        page.operate()
        page.check_point()

    # 校验“质量分析-分析模板-分析规则-删除-EL规则”
    @get_url(analyze_rules_url)
    def test_a153_qualityanalyze_analyzetemplate_analyzerule_delete_el(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_govern_yaml/quality_analyze_yaml/质量分析-分析模板-分析规则-删除-EL规则.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = QualityAnalyzaPage(app)
        page.operate()
        page.check_point()

    # 校验“质量分析-分析模板-分析规则-新建-Extend规则”
    @get_url(analyze_rules_url)
    def test_a154_qualityanalyze_analyzetemplate_analyzerule_create_Extend(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_govern_yaml/quality_analyze_yaml/质量分析-分析模板-分析规则-新建-Extend规则.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = QualityAnalyzaPage(app)
        page.operate()
        page.check_point()

    # 校验“质量分析-分析模板-分析规则-删除-Extend规则”
    @get_url(analyze_rules_url)
    def test_a155_qualityanalyze_analyzetemplate_analyzerule_delete_Extend(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_govern_yaml/quality_analyze_yaml/质量分析-分析模板-分析规则-删除-Extend规则.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = QualityAnalyzaPage(app)
        page.operate()
        page.check_point()

    # 校验“质量分析-分析模板-分析规则-新建-sql规则”
    @get_url(analyze_rules_url)
    def test_a156_qualityanalyze_analyzetemplate_analyzerule_sql_Extend(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_govern_yaml/quality_analyze_yaml/质量分析-分析模板-分析规则-新建-sql规则.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = QualityAnalyzaPage(app)
        page.operate()
        page.check_point()

    # 校验“质量分析-分析模板-分析规则-删除-sql规则”
    @get_url(analyze_rules_url)
    def test_a157_qualityanalyze_analyzetemplate_analyzerule_delete_sql(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_govern_yaml/quality_analyze_yaml/质量分析-分析模板-分析规则-删除-sql规则.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = QualityAnalyzaPage(app)
        page.operate()
        page.check_point()

    # 校验“质量分析-评估结果统计-页面检查”
    @get_url(er_statistics_url)
    def test_a158_qualityanalyze_statistics_page(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_govern_yaml/quality_analyze_yaml/质量分析-评估结果统计-页面检查.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = QualityAnalyzaPage(app)
        page.operate()
        page.check_point()

    # 校验“质量分析-评估结果统计-取消勾选-质量评价-坏数据占比”
    @get_url(er_statistics_url)
    def test_a159_qualityanalyze_statistics_cancel_rate_bad(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_govern_yaml/quality_analyze_yaml/质量分析-评估结果统计-取消勾选-质量评价-坏数据占比.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = QualityAnalyzaPage(app)
        page.operate()
        page.check_point()

    # 校验“质量分析-评估结果统计-图形”
    @get_url(er_statistics_url)
    def test_a160_qualityanalyze_statistics_graph(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_govern_yaml/quality_analyze_yaml/质量分析-评估结果统计-图形.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = QualityAnalyzaPage(app)
        page.operate()
        page.check_point()


    @classmethod
    def setUpClass(cls):
        super(QualityAnalyzeTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(QualityAnalyzeTest, cls).tearDownClass()


################ --------------------------------------------------===================调试区=====================------------------------------------------------------------------------------


# 质量分析页面测试
class QualityAnalyzeTest_SSSS(ParametrizedTestCase):
    execute_info_url = ElementParam.EXECUTE_INFO_URL
    analysis_template_url = ElementParam.ANALYZE_TEMPLATE_URL
    analyze_rules_url = ElementParam.ANALYZE_RULES_URL
    er_statistics_url = ElementParam.ER_STATISTICS_URL

    def login(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/user_for_test/user_dir1.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = LoginTestPage(app)
        page.operate()

    def to_resource_dir(self):
        self.login()
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/质量分析.yaml"),
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

    # 校验“质量分析-分析模板-运行”
    def test_a121_qualityanalyze_mode_run(self):
        self.to_resource_dir()
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_govern_yaml/quality_analyze_yaml/质量分析-分析模板-运行.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = QualityAnalyzaPage(app)
        page.operate()
        page.check_point()

    # 校验“质量分析-任务执行信息-查看日志”
    @get_url(execute_info_url)
    def test_a126_qualityanalyze_taskeexecuteinfo_loginfo(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_govern_yaml/quality_analyze_yaml/质量分析-任务执行信息-查看日志.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = QualityAnalyzaPage(app)
        page.operate()
        page.check_point()

    # 校验“质量分析-任务执行信息-查看日志-关闭”
    @get_url(execute_info_url)
    def test_a127_qualityanalyze_taskeexecuteinfo_loginfo_close(self):
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/data_govern_yaml/quality_analyze_yaml/质量分析-任务执行信息-查看日志-关闭.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = QualityAnalyzaPage(app)
        page.operate()
        page.check_point()

    @classmethod
    def setUpClass(cls):
        super(QualityAnalyzeTest_SSSS, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(QualityAnalyzeTest_SSSS, cls).tearDownClass()