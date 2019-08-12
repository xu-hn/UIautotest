# -*- coding: utf-8 -*-

from common.BaseRunner import ParametrizedTestCase
import unittest, os, sys, time
from PageObject.login.login_page import LoginTestPage
from common.case_false_rerun import rerun
from common.login_who import who_login

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class LoginTest(ParametrizedTestCase):

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

    @get_url()
    def testlogin(self):
        print('1', self.who)
        print('2', who_login(self.who))
        print('3', PATH(who_login(self.who)))

        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH(who_login(self.who)),
               "caseName": sys._getframe().f_code.co_name}
        page = LoginTestPage(app)
        page.operate()
        page.check_point()

    @classmethod
    def setUpClass(cls):
        super(LoginTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(LoginTest, cls).tearDownClass()

if __name__ == "__main__":
    unittest.main()








