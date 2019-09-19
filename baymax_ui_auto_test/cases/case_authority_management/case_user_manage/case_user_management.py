# -*- coding: utf-8 -*-
from common.BaseRunner import ParametrizedTestCase
from PageObject.login.login_page import LoginTestPage
from PageObject.home.home_page import HomePage
import sys, os, time
from common.case_false_rerun import rerun
from common.login_who import who_login
from PageObject.authority_management_page.user_mange_page import AuthorityManagementPage

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), p)
)
# 用户管理页面测试用例
class UserManagementTest(ParametrizedTestCase):

    def login(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH(who_login(self.who)),
               "caseName": sys._getframe().f_code.co_name}
        page = LoginTestPage(app)  # 登录
        page.operate()
        
    def to_resource_dir(self):
        self.login()
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/home/用户管理.yaml"),
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
    
    #校验 ‘用户管理-新建用户’
    @get_url()
    def test_01_user_manage_create_user(self):
        self.to_resource_dir()
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/authority_management_yaml/user_manage_yaml/用户管理-添加用户.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = AuthorityManagementPage(app)
        page.operate()
        page.check_point()
     
    #校验 ‘用户管理-修改用户信息’    
    @get_url()
    def test_02_user_manage_edit_user(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/authority_management_yaml/user_manage_yaml/用户管理-修改用户信息.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = AuthorityManagementPage(app)
        page.operate()
        page.check_point()
          
    #校验 ‘用户管理-修改用户信息’    
    @get_url()
    def test_03_user_manage_edit_user_power(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/authority_management_yaml/user_manage_yaml/用户管理-修改用户权限.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = AuthorityManagementPage(app)
        page.operate()
        page.check_point()
           
#      #校验 ‘用户管理-修改用户有效期’    
    @get_url()
    def test_04_user_manage_edit_user_term_of_validity(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/authority_management_yaml/user_manage_yaml/用户管理-修改用户有效期.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = AuthorityManagementPage(app)
        page.operate()
        page.check_point()
 #校验 ‘用户管理-修改密码有效期’    
    @get_url()
    def test_05_user_manage_edit_user_term_of_validity(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/authority_management_yaml/user_manage_yaml/用户管理-修改密码有效期.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = AuthorityManagementPage(app)
        page.operate()
        page.check_point()
 #校验 ‘用户管理-禁用账户’    
    def test_06_user_manage_prohibit_account(self):
        
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/authority_management_yaml/user_manage_yaml/用户管理-禁用账户.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = AuthorityManagementPage(app)
        page.operate()
        page.check_point()
#校验 ‘用户管理-禁用账户’    
    def test_07_user_manage_enable_account(self):
       
       app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/authority_management_yaml/user_manage_yaml/用户管理-启用账户.yaml"),
              "caseName": sys._getframe().f_code.co_name}
       page = AuthorityManagementPage(app)
       page.operate()
       page.check_point()
#校验 ‘用户管理-禁用账户’    
    def test_08_user_manage_delete_account(self):
      
       app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../YAML/authority_management_yaml/user_manage_yaml/用户管理-删除账户.yaml"),
              "caseName": sys._getframe().f_code.co_name}
       page = AuthorityManagementPage(app)
       page.operate()
       page.check_point()
         
        
# ========================================= 提交 end ========================================================================================


    @classmethod
    def setUpClass(cls):
        super(UserManagementTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(UserManagementTest, cls).tearDownClass()

        