# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
from common.BaseRunner import ParametrizedTestCase
from cases.case_home.case_home_page_click import HomePageTest
from cases.case_login import LoginTest
from cases.case_data_integration.case_resourceMan.case_operate_dir import OperateDirTest
from cases.case_data_integration.case_data_import import DataImportTest
from cases.case_data_integration.case_file_management import FileManagementTest
from cases.case_data_integration.case_collector.case_collector import CollectorTemplateTest, CollectorimportDataTest, CollectorTaskListTest
from cases.case_data_integration.case_file_import.case_file_import import FileImportTest
from cases.case_data_monitor.case_operational_monitoring.case_operational_monitoring import OperationalMonitoringTest
from cases.case_data_monitor.case_task_control.case_task_control import TaskControlTest
from cases.cases_data_govern.case_quality_analyze.case_quality_analyze import QualityAnalyzeTest
from cases.cases_data_govern.case_blood_analyze.case_blood_analyze import BloodAnalyzeTest
from cases.cases_data_govern.case_schema_analyze.case_schema_analyze import SchemaAnalyzeTest
from cases.case_data_analyze.case_flow_management.case_flow_management import FlowManagementTest
from cases.case_data_analyze.case_project_dir.case_project_dir import ProjectDirTest
import unittest
from datetime import datetime
from common.TearDown import mk_file
from common.Count import countDate,writeExcel
from common.Email import send

def runnerCaseApp():
    start_time = datetime.now()
    suite = unittest.TestSuite()
    suite.addTest(ParametrizedTestCase.parametrize(LoginTest))
    suite.addTest(ParametrizedTestCase.parametrize(HomePageTest))
    suite.addTest(ParametrizedTestCase.parametrize(OperateDirTest))
    suite.addTest(ParametrizedTestCase.parametrize(DataImportTest))
    suite.addTest(ParametrizedTestCase.parametrize(FileManagementTest))
    suite.addTest(ParametrizedTestCase.parametrize(FileImportTest))
    suite.addTest(ParametrizedTestCase.parametrize(CollectorTemplateTest))
    suite.addTest(ParametrizedTestCase.parametrize(CollectorimportDataTest))
    suite.addTest(ParametrizedTestCase.parametrize(CollectorTaskListTest))
    suite.addTest(ParametrizedTestCase.parametrize(OperationalMonitoringTest))
    suite.addTest(ParametrizedTestCase.parametrize(TaskControlTest))
    suite.addTest(ParametrizedTestCase.parametrize(QualityAnalyzeTest))
    suite.addTest(ParametrizedTestCase.parametrize(BloodAnalyzeTest))
    suite.addTest(ParametrizedTestCase.parametrize(SchemaAnalyzeTest))
    suite.addTest(ParametrizedTestCase.parametrize(FlowManagementTest))
    suite.addTest(ParametrizedTestCase.parametrize(ProjectDirTest))
    unittest.TextTestRunner(verbosity=2).run(suite)
    end_time = datetime.now()
    countDate(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), str((end_time - start_time).seconds) + "秒")

if __name__ == '__main__':
    mk_file()
    runnerCaseApp()
    writeExcel()
    # send()
