# -*- coding: utf-8 -*-
import unittest, os
from common.Logger import myLog
from selenium import webdriver
from common.ElementParam import ElementParam
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))

# def get_driver():
#     chromedriver = PATH("../exe/chromedriver.exe")
#     os.environ["webdriver.chrome.driver"] = chromedriver
#     chrome_options = Options()
#     chrome_options.add_argument('--headless')
#     driver = webdriver.Chrome(chromedriver, chrome_options=chrome_options)
#     driver.maximize_window()  # 将浏览器最大化
#     # driver = webdriver.Chrome()
#     driver.get(ElementParam.URL)
#     return driver

# chreme headless 模式
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# driver = webdriver.Chrome(chrome_options=chrome_options)

def get_driver():
    
    #设置默认下载路径
    chromeOptions = webdriver.ChromeOptions()
    prefs = {"download.default_directory":"C:\\Users\\Administrator\\Downloads"}
    # chrome 普通模式
    chromedriver = PATH("../exe/chromedriver.exe")
    chromeOptions.add_experimental_option("prefs", prefs)
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver,chrome_options=chromeOptions)

    # #
    # # firefox 普通模式
    # driver = webdriver.Firefox()


    # # firefox headless 模式
    # options = webdriver.FirefoxOptions()
    # options.add_argument('--headless')
    # driver = webdriver.Firefox(options=options)


    driver.maximize_window()  # 将浏览器最大化
    # driver = webdriver.Chrome()
    driver.get(ElementParam.URL)
    el = WebDriverWait(driver, 20, 1).until(lambda x: driver.find_element_by_id("bm-login"))
    who = el.get_attribute('name')
    return driver, who

#原理：写好testcase，然后用testloader加载testcase到testsuite，然后由testrunner运行testsuite，运行的结果保存在texttestresult中
class ParametrizedTestCase(unittest.TestCase):

    def __init__(self, methodName='runTest', param=None):
        super(ParametrizedTestCase, self).__init__(methodName)

    @classmethod  #classmethod类方法，不用生成实例，直接调用类中属性和方法
    #所有测试用例前的设置工作
    def setUpClass(cls): 
        pass
        cls.driver, cls.who = get_driver()
        cls.logTest = myLog().getLog("chrome")  # 每个设备实例化一个日志记录器

    #该测试用例执行前的设置工作
    def setUp(self):
        pass

    @classmethod
    #所有测试用例执行后的清洗工作
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        pass
    #该测试用例执行后的清理工作
    def tearDown(self):
        pass

    @staticmethod #@staticmethod 不需要传cls参数
    def parametrize(testcase_klass, param=None):
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase_klass)
        suite = unittest.TestSuite()
        for name in testnames:
            suite.addTest(testcase_klass(name, param=param))
        return suite
