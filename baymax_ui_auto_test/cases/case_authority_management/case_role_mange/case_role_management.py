# -*- coding: utf-8 -*-
from common.BaseRunner import ParametrizedTestCase
from PageObject.login.login_page import LoginTestPage
from PageObject.home.home_page import HomePage
import sys, os, time
from common.case_false_rerun import rerun
from common.login_who import who_login
from PageObject.authority_management_page.role_mange_page import AuthorityManagementPage

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), p)
)


# 权限管理页面测试用例
class RoleManagementTest(ParametrizedTestCase):

    def login(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH(who_login(self.who)),
               "caseName": sys._getframe().f_code.co_name}
        page = LoginTestPage(app)  # 登录
        page.operate()

    def to_resource_dir(self):
        self.login()
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/角色管理.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = HomePage(app)  # page页实例化
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

    # 校验“角色管理-新建角色”
    @get_url()
    def test_01_role_manage_create_role(self):
        self.to_resource_dir()
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/authority_management_yaml/role_mange_yaml/角色管理-添加角色.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = AuthorityManagementPage(app)
        page.operate()
        page.check_point()

    # 校验“角色管理-禁用角色”
    @get_url()
    def test_02_role_manage_disable_role(self):
        #self.to_resource_dir()
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/authority_management_yaml/role_mange_yaml/角色管理-禁用角色.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = AuthorityManagementPage(app)
        page.operate()
        page.check_point()
        
    #校验‘角色管理-删除角色’
    def test_03_role_manage_delete_role(self):
        #self.to_resource_dir()
        app = {"logTest": self.logTest, "driver": self.driver,
               "path": PATH("../YAML/authority_management_yaml/role_mange_yaml/角色管理-删除角色.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = AuthorityManagementPage(app)
        page.operate()
        page.check_point()
# ========================================= 提交 end ========================================================================================


    @classmethod
    def setUpClass(cls):
        super(RoleManagementTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(RoleManagementTest, cls).tearDownClass()
