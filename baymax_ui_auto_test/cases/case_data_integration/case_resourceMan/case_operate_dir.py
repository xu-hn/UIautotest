# -*- coding: utf-8 -*-

from common.BaseRunner import ParametrizedTestCase
import unittest, os, sys, time
from PageObject.data_integration_page.resourceMan_page.resourceMan_page import ResourceManPage
from PageObject.home.home_page import HomePage
from PageObject.login.login_page import LoginTestPage
from common.ElementParam import ElementParam
from common.case_false_rerun import rerun
from common.login_who import who_login

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), p)
)

class OperateDirTest(ParametrizedTestCase):
    resourceMan_url = ElementParam.RESOURCE_MEN_URL

    def login(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path":  PATH(who_login(self.who)),
               "caseName": sys._getframe().f_code.co_name}
        page = LoginTestPage(app)
        page.operate()

    def to_resource_dir(self):
        self.login()
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/资源目录.yaml"),
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

    # 校验“打开数据标准文件夹”
    @get_url()
    def test_a017_open_dir(self):
        self.to_resource_dir()
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/resourceMan_yaml/展开文件夹.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ResourceManPage(app)
        page.operate()
        page.check_point()

    # 校验“闭合数据标准文件夹”
    @get_url(resourceMan_url)
    def test_a018_close_dir(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/resourceMan_yaml/闭合文件夹.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ResourceManPage(app)
        page.operate()
        page.check_point()

    # 校验“新建数据标准文件夹”
    @get_url(resourceMan_url)
    def test_a019_create_dir(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/resourceMan_yaml/新建文件夹.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ResourceManPage(app)
        page.operate()
        page.check_point()

     # 校验“删除数据标准文件夹”
    @get_url(resourceMan_url)
    def test_a020_delete_dir(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/resourceMan_yaml/删除文件夹.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ResourceManPage(app)
        page.operate()
        page.check_point()

    # 校验“移动数据标准文件夹”
    @get_url(resourceMan_url)
    def test_a021_move_dir(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/resourceMan_yaml/移动文件夹.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ResourceManPage(app)
        page.operate()
        page.check_point()

    # 校验“创建jdbc数据源”
    @get_url(resourceMan_url)
    def test_a022_create_dbsource_jdbc(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/resourceMan_yaml/数据源-新建JDBC数据源.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ResourceManPage(app)
        page.operate()
        page.check_point()

    # 校验“创建jdbc_oracle数据源”
    @get_url(resourceMan_url)
    def test_b002_create_dbsource_jdbc_oracle(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/resourceMan_yaml/数据源-新建JDBC_oracle数据源.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ResourceManPage(app)
        page.operate()
        page.check_point()

    # 校验“创建jdbc_hive数据源”
    @get_url(resourceMan_url)
    def test_b003_create_dbsource_jdbc_hive(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/resourceMan_yaml/数据源-新建JDBC_hive数据源.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ResourceManPage(app)
        page.operate()
        page.check_point()

    # 校验“创建_http_数据源”
    @get_url(resourceMan_url)
    def test_b004_create_source_http(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/resourceMan_yaml/数据源-新建_http_数据源.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ResourceManPage(app)
        page.operate()
        page.check_point()

    # 校验“创建_ftp_数据源”
    @get_url(resourceMan_url)
    def test_b005_create_source_ftp(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/resourceMan_yaml/数据源-新建_ftp_数据源.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ResourceManPage(app)
        page.operate()
        page.check_point()

    # 校验“创建_socket_数据源”
    @get_url(resourceMan_url)
    def test_b006_create_source_socket(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/resourceMan_yaml/数据源-新建_SOCKET_数据源.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ResourceManPage(app)
        page.operate()
        page.check_point()

    # 校验“创建_mongodb_数据源”
    @get_url(resourceMan_url)
    def test_b007_create_source_mongodb(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/resourceMan_yaml/数据源-新建_mongodb_数据源.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ResourceManPage(app)
        page.operate()
        page.check_point()

    # 校验“创建_ElasticSearch_数据源”
    @get_url(resourceMan_url)
    def test_b008_create_source_ElasticSearch(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/resourceMan_yaml/数据源-新建_ElasticSearch_数据源.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ResourceManPage(app)
        page.operate()
        page.check_point()

    # 校验“创建jdbc_oracle数据源_链接测试”
    @get_url(resourceMan_url)
    def test_b009_create_dbsource_jdbc_oracle_connect(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/resourceMan_yaml/数据源-新建JDBC_oracle数据源_链接测试.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ResourceManPage(app)
        page.operate()
        page.check_point()


    # 校验“创建jdbc_hive数据源_链接测试”
    @get_url(resourceMan_url)
    def test_b010_create_dbsource_jdbc_hive_connect(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/resourceMan_yaml/数据源-新建JDBC_hive数据源_链接测试.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ResourceManPage(app)
        page.operate()
        page.check_point()

    # 校验“创建jdbc数据源-链接测试”
    @get_url()
    def test_a023_create_dbsource_jdbc_connect(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/resourceMan_yaml/数据源-新建JDBC数据源-链接测试.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ResourceManPage(app)
        page.operate()
        page.check_point()

    # 校验“删除jdbc数据源”
    @get_url()
    def test_a024_delete_dbsource_jdbc(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/resourceMan_yaml/数据源-删除JDBC数据源.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ResourceManPage(app)
        page.operate()
        page.check_point()

    # 校验“元数据-新建schema”
    @get_url()
    def test_a025_create_schema(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/resourceMan_yaml/元数据-新建schema.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ResourceManPage(app)
        page.operate()
        page.check_point()

    # 校验“元数据-移动schema”
    @get_url()
    def test_a026_move_schema(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/resourceMan_yaml/元数据-移动schema.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ResourceManPage(app)
        page.operate()
        page.check_point()

    # 校验“元数据-复制schema”
    @get_url()
    def test_a027_copy_schema(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/resourceMan_yaml/元数据-复制schema.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ResourceManPage(app)
        page.operate()
        page.check_point()

    # 校验“元数据-删除schema”
    @get_url()
    def test_a028_delete_schema(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/resourceMan_yaml/元数据-删除schema.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ResourceManPage(app)
        page.operate()
        page.check_point()

    # 校验“元数据-分析-新建schema”
    @get_url()
    def test_a029_analysis_create_schema(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/resourceMan_yaml/元数据-分析-新建schema.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ResourceManPage(app)
        page.operate()
        page.check_point()

    # 校验“数据集-新建_mysql_Dataset”
    @get_url(resourceMan_url)
    def test_a030_create_Dataset(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/resourceMan_yaml/数据集-新建Dataset.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ResourceManPage(app)
        page.operate()
        page.check_point()

    # 校验“数据集-新建_Oracle_Dataset”
    @get_url(resourceMan_url)
    def test_b001_create_Oracle_Dataset(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/resourceMan_yaml/数据集-新建-Oracle-Dataset.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ResourceManPage(app)
        page.operate()
        page.check_point()

    # 校验“数据集-移动Dataset”
    @get_url()
    def test_a031_move_Dataset(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/resourceMan_yaml/数据集-移动Dataset.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ResourceManPage(app)
        page.operate()
        page.check_point()

    # 校验“数据集-删除Dataset”
    @get_url()
    def test_a032_delete_Dataset(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/resourceMan_yaml/数据集-删除Dataset.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ResourceManPage(app)
        page.operate()
        page.check_point()

    # 校验“数据集-预览Dataset”
    @get_url()
    def test_a033_preview_Dataset(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/resourceMan_yaml/数据集-预览Dataset.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ResourceManPage(app)
        page.operate()
        page.check_point()

    # 校验“数据集-查看Dataset”
    @get_url(resourceMan_url)
    def test_a034_view_Dataset(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/resourceMan_yaml/数据集-查看Dataset.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ResourceManPage(app)
        page.operate()
        page.check_point()

    # 校验“数据集-新建HDFSDataset”
    @get_url(resourceMan_url)
    def test_a035_create_HDFSDataset(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/resourceMan_yaml/数据集-新建HDFSDataset.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ResourceManPage(app)
        page.operate()
        page.check_point()

    # 校验“数据集-移动HDFSDataset”
    @get_url(resourceMan_url)
    def test_a036_move_HDFSDDataset(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/resourceMan_yaml/数据集-移动HDFSDataset.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ResourceManPage(app)
        page.operate()
        page.check_point()

    # 校验“数据集-删除HDFSDataset”
    @get_url(resourceMan_url)
    def test_a037_delete_HDFSDataset(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/resourceMan_yaml/数据集-删除HDFSDataset.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ResourceManPage(app)
        page.operate()
        page.check_point()

    # 校验“数据集-预览HDFSDataset”
    @get_url()
    def test_a038_preview_HDFSDataset(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/resourceMan_yaml/数据集-预览HDFSDataset.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ResourceManPage(app)
        page.operate()
        page.check_point()

    # 校验“数据集-查看HDFSDataset”
    @get_url(resourceMan_url)
    def test_a039_view_HDFSDataset(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/resourceMan_yaml/数据集-查看HDFSDataset.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ResourceManPage(app)
        page.operate()
        page.check_point()

    # 校验“数据标准-新建standard”
    @get_url(resourceMan_url)
    def test_a040_create_standard(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/resourceMan_yaml/数据标准-新建standard.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ResourceManPage(app)
        page.operate()
        page.check_point()

    # 校验“数据标准-移动standard”
    @get_url()
    def test_a041_move_standard(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/resourceMan_yaml/数据标准-移动standard.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ResourceManPage(app)
        page.operate()
        page.check_point()

    # 校验“数据标准-删除standard”
    @get_url()
    def test_a042_delete_standard(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/resourceMan_yaml/数据标准-删除standard.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ResourceManPage(app)
        page.operate()
        page.check_point()

    @classmethod
    def setUpClass(cls):
        super(OperateDirTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(OperateDirTest, cls).tearDownClass()

'''
    ---------------------------------------                        调试                              --------------------------------------------------------------------------------------------
'''
class OperateDirTestSSSS(ParametrizedTestCase):
    resourceMan_url = ElementParam.RESOURCE_MEN_URL

    def login(self):
        app = {"logTest": self.logTest, "driver": self.driver,  "path":  PATH(who_login(self.who)),
               "caseName": sys._getframe().f_code.co_name}
        page = LoginTestPage(app)
        page.operate()

    def to_resource_dir(self):
        self.login()
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/资源目录.yaml"),
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

    # 校验“打开数据标准文件夹”
    def test_a017_open_dir(self):
        self.to_resource_dir()

        # 校验“移动数据标准文件夹”
    @get_url(resourceMan_url)
    def test_a021_move_dir(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/data_integration_yaml/resourceMan_yaml/移动文件夹.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = ResourceManPage(app)
        page.operate()
        page.check_point()



    @classmethod
    def setUpClass(cls):
        super(OperateDirTestSSSS, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(OperateDirTestSSSS, cls).tearDownClass()

if __name__ == "__main__":
    unittest.main()