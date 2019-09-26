# -*- coding: utf-8 -*-
from common.ElementParam import ElementParam as ep
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import selenium.common.exceptions
from selenium.webdriver.common.action_chains import ActionChains
import time, os, re, subprocess
from selenium.webdriver.common.keys import Keys
from common.operate_time import to_time_stamp

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class OperateElement():

    def __init__(self, driver=''):
        self.driver = driver
        # self.driver = webdriver.Chrome()

    def findElement(self, operate):
        try:
            if type(operate) == list:
                for item in operate:
                    t = item['check_time'] if item.get('check_time', 0) != 0 else ep.WAIT_TIME
                    WebDriverWait(self.driver, t).until(lambda x: self.element_by(item))
                return {'result': True}
            if type(operate) == dict:
                '''
                if operate.get('element_info', 0) == 0:
                    return {'result': True}
                如果有元素 yaml文档不要忘记写element_info！！！
                '''
                if operate.get('element_info', 0) == 0: # 如果没有页面元素，就不检测是页面元素，可能是滑动等操作
                    return {'result': True}
                t = operate['check_time'] if operate.get('check_time', 0) != 0 else ep.WAIT_TIME
                el = WebDriverWait(self.driver, t, 1).until(lambda x: self.element_by(operate))
                print('找到了element：', operate['info'])
                print(el)
                return {'result': True}
        except selenium.common.exceptions.TimeoutException as msg:
            print('TimeoutException:===========', msg)
            return {'result': False, 'type': ep.TIME_OUT}
        except selenium.common.exceptions.NoSuchElementException:
            return {'result': False, 'type': ep.NO_SUCH}
        except selenium.common.exceptions.WebDriverException:
            return {'result': False, 'type': ep.WEB_DROVER_EXCEPTION}
    '''
    {'element_info': 'input-lg', 'find_type': 'class_name', 'operate_type': 'send_keys', 'msg': 'lose1', 'info': '输入用户名lose1'}
    [{'id': 'test001', 'title': '登录失败', 'launch': 1, 'info': '打开testerhome'}]
    <Base.BaseLog.Log object at 0x00000000037F8BA8>
    '''
    def operate(self, operate, testInfo, logTest):
        res = self.findElement(operate)
        print(res)
        if res["result"]:
            return self.operate_by(operate, testInfo, logTest)
        else:
            return res

    def operate_by(self, operate, testInfo, logTest):
        try:
            info = '__%s__%s__%s__%s__' % (operate.get('element_info', ' '), operate.get('find_type', ' '),
                                    operate.get('operate_type', ' '), operate.get('msg', ' '))
            logTest.buildStartLine(str(testInfo[0]['id']) + "__" + testInfo[0]['title']+ "_" + info)
            if operate.get('operate_type', 0) == 0: # 一般为检查点，不需要操作，直接返回true
                print('---------没有找到operate_type在：----应该为检查点-----info为：', operate['info'])
                return {'result': True}
            elements = {
                ep.CLICK: lambda: self.click_opetate(operate),
                ep.SEND_KEYS: lambda: self.send_keys(operate),
                ep.ACTION_CHAINS: lambda: self.action_chains(operate),
                ep.MOVE_BY_OFFSET: lambda: self.move_mouse(operate),
                ep.GET_TEXT: lambda: self.get_text(operate),
                ep.GET_VALUE: lambda: self.get_value(operate),
                ep.GET_CURRENT_URL: lambda: self.get_current_url(operate),
                ep.GET_ATTR: lambda: self.get_attr(operate),
                ep.IS_DISPLAYED: lambda: self.displayed(operate),
                ep.FIND_DOWN: lambda: self.find_element_down(operate),
                ep.MOVE_SCROLLBAR_BOTTOM: lambda: self.move_scrollbar_bottom(operate),
                ep.UPLOAD_FILE: lambda: self.upload_file(operate),
                ep.DOWNLOAD_FILE: lambda: self.download_file(operate),
                ep.REFRESH_GET_TEXT: lambda: self.refresh_get_text(operate),
                ep.REFRESH_GET_ATTR: lambda: self.refresh_get_attr(operate),
                ep.REFRESH_TIME_DIFFERENCE: lambda: self.refresh_time_difference(operate),
                ep.REFRESH_GET_TEXT_IS_EXPECT: lambda: self.refresh_get_text_is_expect(operate),
                ep.TO_IFRAME: lambda: self.to_iframe(operate),
                ep.DEFAULT_CONTENT: lambda: self.switch_default_content(),
                ep.REFRESH: lambda: self.refresh(),
                ep.CLEAR: lambda: self.clear(operate),
                ep.TO_URL: lambda: self.to_url(operate),
                ep.TO_WINDOW: lambda: self.to_window(operate),
                ep.CLOSE_WINDOW: lambda: self.close_window(),
                ep.DRAG_EL: lambda: self.drag_el(operate),
                ep.DOUBLE_CLICK: lambda: self.double_click_opetate(operate),
                ep.KEY_OPETATE: lambda: self.key_operate(operate),

            }
            return elements[operate['operate_type']]()

        # except IndexError:
        #     logTest.buildStartLine(
        #         testInfo[0]["id"] + "_" + testInfo[0]["title"] + "_" + operate["element_info"] + "索引错误")  # 记录日志
        #     # print(operate["element_info"] + "索引错误")
        #     return {"result": False, "type": be.INDEX_ERROR}
        #
        # except selenium.common.exceptions.NoSuchElementException:
        #     logTest.buildStartLine(
        #         testInfo[0]["id"] + "_" + testInfo[0]["title"] + "_" + operate[
        #             "element_info"] + "页面元素不存在或没加载完成")  # 记录日志
        #     # print(operate["element_info"] + "页面元素不存在或没有加载完成")
        #     return {"result": False, "type": be.NO_SUCH}
        # except selenium.common.exceptions.StaleElementReferenceException:
        #     logTest.buildStartLine(
        #         testInfo[0]["id"] + "_" + testInfo[0]["title"] + "_" + operate[
        #             "element_info"] + "页面元素已经变化")  # 记录日志
        #     # print(operate["element_info"] + "页面元素已经变化")
        #     return {"result": False, "type": be.STALE_ELEMENT_REFERENCE_EXCEPTION}
        except KeyError:
            logTest.buildStartLine(
                testInfo[0]['id'] + '__' + testInfo[0]["title"] + "__" + operate[
                     "element_info"] +"__" + 'Operate缺少key, 或者key写错了'
            )
            return {"result": False}
        except Exception as msg:
            print(msg)
            msg = str(msg)
            logTest.buildStartLine(
                testInfo[0]['id'] + '__' + testInfo[0]["title"] + "__" +
                operate["element_info"] +"__" + '没定位的错误' + msg
            )
            return {'result': False}

    # 跳转到某URL
    def to_url(self, operate):
        url = ep.HOST + operate["url"]
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        return {'result': True}

    # 清除输入框
    def clear(self, operate):
        if operate['find_type'] == ep.find_element_by_id or operate['find_type'] == ep.find_element_by_xpath or \
            operate['find_type'] == ep.find_element_by_name or operate['find_type'] == ep.find_element_by_class_name:
            self.element_by(operate).clear()
        elif operate['find_type'] == ep.find_elements_by_id or operate['find_type'] == ep.find_elements_by_xpath or \
            operate['find_type'] == ep.find_elements_by_name or operate['find_type'] == ep.find_elements_by_class_name:
            self.element_by(operate)[operate["index"]].clear()
        return {'result': True}

    # 键盘操作
    def key_operate(self, operate):
        if operate['find_type'] == ep.find_element_by_id or operate['find_type'] == ep.find_element_by_xpath or \
            operate['find_type'] == ep.find_element_by_name or operate['find_type'] == ep.find_element_by_class_name:
            if operate.get('key_c', 'aaaaaaaaaaaaaaaa') !=  'aaaaaaaaaaaaaaaa':
                keys = {
                    "CONTROL": lambda: self.element_by(operate).send_keys(Keys.CONTROL, operate['key_c']),
                }
                try:
                    keys[operate['key_s']]()
                except KeyError:
                    print('==================key不对哦！=====================================')
                    return {'result': False}
            else:
                keys = {
                    "DELETE": lambda: self.element_by(operate).send_keys(Keys.DELETE),
                }
                try:
                    keys[operate['key_s']]()
                except KeyError:
                    print('==================key不对哦！=====================================')
                    return {'result': False}
        elif operate['find_type'] == ep.find_elements_by_id or operate['find_type'] == ep.find_elements_by_xpath or \
            operate['find_type'] == ep.find_elements_by_name or operate['find_type'] == ep.find_elements_by_class_name:
            if operate.get('key_c', 'aaaaaaaaaaaaaaaa') !=  'aaaaaaaaaaaaaaaa':
                keys = {
                    "CONTROL": lambda: self.element_by(operate)[operate["index"]].send_keys(Keys.CONTROL, operate['key_c']),
                }
                try:
                    keys[operate['key_s']]()
                except KeyError:
                    print('==================key不对哦！=====================================')
                    return {'result': False}
            else:
                keys = {
                    "DELETE": lambda: self.element_by(operate)[operate["index"]].send_keys(Keys.DELETE),
                }
                try:
                    keys[operate['key_s']]()
                except KeyError:
                    print('==================key不对哦！=====================================')
                    return {'result': False}
        return {'result': True}

    # 切换window
    def to_window(self, operate):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[operate['w_index']])
        return {'result': True}

    # 关闭window
    def close_window(self):
        self.driver.close()
        return {'result': True}

    #  切换到iframe
    def to_iframe(self, operate):
        if operate['find_type'] == ep.find_element_by_id or operate['find_type'] == ep.find_element_by_xpath or \
            operate['find_type'] == ep.find_element_by_name or operate['find_type'] == ep.find_element_by_class_name:
            self.driver.switch_to.frame(self.element_by(operate))
        elif operate['find_type'] == ep.find_elements_by_id or operate['find_type'] == ep.find_elements_by_xpath or \
            operate['find_type'] == ep.find_elements_by_name or operate['find_type'] == ep.find_elements_by_class_name:
            self.driver.switch_to.frame(self.element_by(operate)[operate["index"]])
        return {'result': True}

    # 从iframe切换回当前content
    def switch_default_content(self):
        self.driver.switch_to.default_content()
        return {'result': True}

    # 刷新当前页面
    def refresh(self):
        self.driver.refresh()
        return {'result': True}

    # 刷新页面 直到页面变化或超时 返回最后的text
    def refresh_get_text(self, operate):
        old_text =self.get_text(operate)["text"]
        time_out = int(operate["time_out"])
        cs_time = 0
        s_time = time.time()
        while time_out > cs_time:
            self.driver.refresh()
            time.sleep(2)
            # self.driver.implicitly_wait(3)
            new_text =self.get_text(operate)["text"]
            if new_text != old_text:
                return {'result': True, 'text': new_text}
            time.sleep(1)
            cs_time = int(time.time() - s_time)
        return {'result': False, 'text': new_text}

    # 刷新页面 获取的值符合预期 返回最后的text
    def refresh_get_text_is_expect(self, operate):
        old_text =self.get_text(operate)["text"]
        if old_text not in operate["expect_values"]:
            return {'result': False, 'text': old_text}
        time_out = int(operate["time_out"])
        cs_time = 0
        s_time = time.time()
        while time_out > cs_time:
            self.driver.refresh()
            time.sleep(2)
            # self.driver.implicitly_wait(3)
            new_text =self.get_text(operate)["text"]
            if new_text == operate["expect_value"]:
                return {'result': True, 'text': new_text}
            time.sleep(1)
            cs_time = int(time.time() - s_time)
        return {'result': False, 'text': new_text}

     # 刷新页面 直到页面属性变化或超时 返回最后的text
    def refresh_get_attr(self, operate):
        old_text =self.get_attr(operate)["text"]
        time_out = int(operate["time_out"])
        cs_time = 0
        s_time = time.time()
        while time_out > cs_time:
            self.driver.refresh()
            time.sleep(2)
            # self.driver.implicitly_wait(3)
            new_text =self.get_attr(operate)["text"]
            if new_text != old_text:
                return {'result': True, 'text': new_text}
            time.sleep(1)
            cs_time = int(time.time() - s_time)
        return {'result': False, 'text': new_text}

    # 刷新页面直到时间差小于预期值
    def refresh_time_difference(self, operate):
        time_out = int(operate["time_out"])
        cs_time = 0
        s_time = time.time()
        while time_out > cs_time:
            self.driver.refresh()
            time.sleep(1)
            # self.driver.implicitly_wait(3)
            new_text =self.get_text(operate)["text"]
            if (time.time() - to_time_stamp(f_time=new_text)) < operate["max_time"]:
                return {'result': True, 'text': new_text}
            # time.sleep(1)
            cs_time = int(time.time() - s_time)
        return {'result': False, 'text': new_text}

    # 上传文件 使用autoit可执行文件
    def upload_file(self, operate):
        main = PATH("../exe/" + operate["file_name"])
        print(main)
        if os.path.exists(main):
            rc,out= subprocess.getstatusoutput(main)
            if not rc:
                return {'result': True}
            else:
                print('执行状态为:', rc,'错误msg: ', out)
                return {'result': False}
        else:
            print(main, "路径不存在！！！")
            return {'result': False}
    #下载文件  判断路径下文件是否存在
    def download_file(self,operate):
        main = "C:/Users/Administrator/Downloads"
        files = os.listdir(main)
        print(main)
        for f in files:
            if f.endswith('.woven') and (operate["file_name"] in f):
                print('文件存在')
                return {'result': True}
            else:
                print(main,'路径或文件不存在')
                return{"result": False}
        

    # 检查元素是否显示
    def displayed(self, operate):
        if operate['find_type'] == ep.find_element_by_id or operate['find_type'] == ep.find_element_by_xpath or \
            operate['find_type'] == ep.find_element_by_name or operate['find_type'] == ep.find_element_by_class_name:
            result = self.element_by(operate).is_displayed()
            print('检查元素是否显示++++++++++++++++++++++++++++', result)
            return {'result': result}
        elif operate['find_type'] == ep.find_elements_by_id or operate['find_type'] == ep.find_elements_by_xpath or \
            operate['find_type'] == ep.find_elements_by_name or operate['find_type'] == ep.find_elements_by_class_name:
            result = self.element_by(operate)[operate['index']].is_displayed()
            print('检查元素是否显示++++++++++++++++++++++++++++', result)
            return {'result': result}

    # 获取当前的URL
    def get_current_url(self, operate):
        url = self.driver.current_url
        return {'result': True, 'text': url}

    # 拖拽元素
    def drag_el(self, operate):
        action_chains = ActionChains(self.driver)
        if operate['find_type'] == ep.find_element_by_id or operate['find_type'] == ep.find_element_by_xpath or \
            operate['find_type'] == ep.find_element_by_name or operate['find_type'] == ep.find_element_by_class_name:
            A = self.element_by(operate)
        elif operate['find_type'] == ep.find_elements_by_id or operate['find_type'] == ep.find_elements_by_xpath or \
            operate['find_type'] == ep.find_elements_by_name or operate['find_type'] == ep.find_elements_by_class_name:
            A = self.element_by(operate)[operate['index']]
        if operate.get('find_type2') and operate.get('element_info2'):
            if operate['find_type2'] == ep.find_element_by_id or operate['find_type2'] == ep.find_element_by_xpath or \
                operate['find_type2'] == ep.find_element_by_name or operate['find_type2'] == ep.find_element_by_class_name:
                B = self.element_by2(operate)
            elif operate['find_type2'] == ep.find_elements_by_id or operate['find_type2'] == ep.find_elements_by_xpath or \
                operate['find_type2'] == ep.find_elements_by_name or operate['find_type2'] == ep.find_elements_by_class_name:
                B = self.element_by2(operate)[operate['index2']]
            # 将元素A 拖拽到 元素B
            action_chains.drag_and_drop(A, B).perform()
            return {'result': True}
        elif operate.get("move_to"):
            # 元素A 拖拽到某个像素
            action_chains.drag_and_drop_by_offset(self.element_by(operate), *tuple(eval(operate['move_to']))).perform()
            return {'result': True}
        print("缺少find_type2 或者 element_info2 或者 move_to")
        return {'result': False}


    # 移动鼠标到某个像素
    def move_mouse(self, operate):
        ActionChains(self.driver).move_by_offset(*tuple(eval(operate['move_to']))).perform()
        return {'result': True}

    # 输入文字操作
    def send_keys(self, operate):
        if operate['find_type'] == ep.find_element_by_id or operate['find_type'] == ep.find_element_by_xpath or \
            operate['find_type'] == ep.find_element_by_name or operate['find_type'] == ep.find_element_by_class_name:
            print('-----------操作sendkeys之前---------------')
            print(operate['msg'])
            self.element_by(operate).send_keys(operate['msg'])
        elif operate['find_type'] == ep.find_elements_by_id or operate['find_type'] == ep.find_elements_by_xpath or \
            operate['find_type'] == ep.find_elements_by_name or operate['find_type'] == ep.find_elements_by_class_name:
            self.element_by(operate)[operate['index']].send_keys(operate['msg'])
        return {'result': True}

    # 点击操作
    def click_opetate(self, operate):
        if operate['find_type'] == ep.find_element_by_id or operate['find_type'] == ep.find_element_by_xpath or \
            operate['find_type'] == ep.find_element_by_name or operate['find_type'] == ep.find_element_by_class_name:
            # self.element_by(operate).click()
            # return {'result': True}
            try:
                self.element_by(operate).click()
                return {'result': True}
            except selenium.common.exceptions.ElementClickInterceptedException:
                print('抓到了这个错：is not clickable at point')
                time.sleep(1)
                self.element_by(operate).click()
                return {'result': True}
        elif operate['find_type'] == ep.find_elements_by_id or operate['find_type'] == ep.find_elements_by_xpath or \
            operate['find_type'] == ep.find_elements_by_name or operate['find_type'] == ep.find_elements_by_class_name:
            # self.element_by(operate)[operate['index']].click()
            # return {'result': True}
            try:
                self.element_by(operate)[operate['index']].click()
                return {'result': True}
            except selenium.common.exceptions.ElementClickInterceptedException:
                print('抓到了这个错：is not clickable at point')
                time.sleep(1)
                self.element_by(operate)[operate['index']].click()
                return {'result': True}

    # 双击操作
    def double_click_opetate(self, operate):
        action_chains = ActionChains(self.driver)
        if operate['find_type'] == ep.find_element_by_id or operate['find_type'] == ep.find_element_by_xpath or \
            operate['find_type'] == ep.find_element_by_name or operate['find_type'] == ep.find_element_by_class_name:
            action_chains.double_click(self.element_by(operate)).perform()
            return {'result': True}
        elif operate['find_type'] == ep.find_elements_by_id or operate['find_type'] == ep.find_elements_by_xpath or \
            operate['find_type'] == ep.find_elements_by_name or operate['find_type'] == ep.find_elements_by_class_name:
            action_chains.double_click(self.element_by(operate)[operate['index']]).perform()
            return {'result': True}

    #鼠标悬停事件
    def action_chains(self, operate):
        if operate['find_type'] == ep.find_element_by_id or operate['find_type'] == ep.find_element_by_xpath or \
            operate['find_type'] == ep.find_element_by_name or operate['find_type'] == ep.find_element_by_class_name:
            ActionChains(self.driver).move_to_element(self.element_by(operate)).perform()
            time.sleep(0.7)
            return {'result': True}
        elif operate['find_type'] == ep.find_elements_by_id or operate['find_type'] == ep.find_elements_by_xpath or \
            operate['find_type'] == ep.find_elements_by_name or operate['find_type'] == ep.find_elements_by_class_name:
            ActionChains(self.driver).move_to_element(self.element_by(operate)[operate['index']]).perform()
            time.sleep(0.7)
            return {'result': True}

    def get_value(self, operate):
        if operate['find_type'] == ep.find_element_by_id or operate['find_type'] == ep.find_element_by_xpath or \
            operate['find_type'] == ep.find_element_by_name or operate['find_type'] == ep.find_element_by_class_name:
            re_value = re.findall(r'[:.\-_a-zA-Z\d+\u4e00-\u9fa5]', self.element_by(operate).get_attribute('value'))
            value = ''.join(re_value)
            print('获取到的值为：', value)
            return {'result': True, 'text': value}
        elif operate['find_type'] == ep.find_elements_by_id or operate['find_type'] == ep.find_elements_by_xpath or \
            operate['find_type'] == ep.find_elements_by_name or operate['find_type'] == ep.find_elements_by_class_name:
            re_value = re.findall(r'[:.\-_a-zA-Z\d+\u4e00-\u9fa5]', self.element_by(operate)[operate['index']].get_attribute('value'))
            value = ''.join(re_value)
            print('获取到的值为：', value)
            return {'result': True, 'text': value}


    def get_text(self, operate):
        if operate['find_type'] == ep.find_element_by_id or operate['find_type'] == ep.find_element_by_xpath or \
            operate['find_type'] == ep.find_element_by_name or operate['find_type'] == ep.find_element_by_class_name:
            re_reulst = re.findall(r'[:.\-_a-zA-Z\d+\u4e00-\u9fa5]', self.element_by(operate).text)
            text = ''.join(re_reulst)
            print('获取到的值为：', text)
            if text == "":
                text = "None"
                print('text是none类型转化的值为：', text)
            return {'result': True, 'text': text}
        elif operate['find_type'] == ep.find_elements_by_id or operate['find_type'] == ep.find_elements_by_xpath or \
            operate['find_type'] == ep.find_elements_by_name or operate['find_type'] == ep.find_elements_by_class_name:
            re_reulst = re.findall(r'[:.\-_a-zA-Z\d+\u4e00-\u9fa5]', self.element_by(operate)[operate['index']].text)
            text = ''.join(re_reulst)
            print('获取到的值为：', text)
            print(type(text))
            if text == "":
                text = "None"
                print('text是none类型转化的值为：', text)
            return {'result': True, 'text': text}

    def get_attr(self, operate):
        if operate['find_type'] == ep.find_element_by_id or operate['find_type'] == ep.find_element_by_xpath or \
            operate['find_type'] == ep.find_element_by_name or operate['find_type'] == ep.find_element_by_class_name:
            text = self.element_by(operate).get_attribute(operate['attr'])
            print('获取到的值为：', text)
            text = str(text)
            return {'result': True, 'text': text}
        elif operate['find_type'] == ep.find_elements_by_id or operate['find_type'] == ep.find_elements_by_xpath or \
            operate['find_type'] == ep.find_elements_by_name or operate['find_type'] == ep.find_elements_by_class_name:
            text =  self.element_by(operate)[operate['index']].get_attribute(operate['attr'])
            print('获取到的值为：', text)
            text = str(text)
            return {'result': True, 'text': text}

    # 在下拉菜单中 向下查找元素 直到元素出现
    def find_element_down(self, operate):
        if operate['find_type'] == ep.find_element_by_id or operate['find_type'] == ep.find_element_by_xpath or \
            operate['find_type'] == ep.find_element_by_name or operate['find_type'] == ep.find_element_by_class_name:
            start_time = time.time()
            while True:
                self.element_by(operate).send_keys(Keys.DOWN)
                time.sleep(0.1)
                if operate['find_type2'] == ep.find_element_by_id or operate['find_type2'] == ep.find_element_by_xpath or \
            operate['find_type2'] == ep.find_element_by_name or operate['find_type2'] == ep.find_element_by_class_name:
                    result = self.element_by2(operate).text
                elif operate['find_type2'] == ep.find_elements_by_id or operate['find_type2'] == ep.find_elements_by_xpath or \
            operate['find_type2'] == ep.find_elements_by_name or operate['find_type2'] == ep.find_elements_by_class_name:
                    result = self.element_by2(operate)[operate['index']].text
                re_reulst = re.findall(r'[:.\-_a-zA-Z\d+\u4e00-\u9fa5]', result)
                text = ''.join(re_reulst)
                print('33333333333::::::::',text)
                if text == operate["find_v"]:
                    time.sleep(1)
                    return {'result': True}
                if time.time()-start_time > operate['find_time_out']:
                    return {'result': False}
        elif operate['find_type'] == ep.find_elements_by_id or operate['find_type'] == ep.find_elements_by_xpath or \
            operate['find_type'] == ep.find_elements_by_name or operate['find_type'] == ep.find_elements_by_class_name:
            start_time = time.time()
            while True:
                self.element_by(operate)[operate['index']].send_keys(Keys.DOWN)
                time.sleep(0.1)
                if operate['find_type2'] == ep.find_element_by_id or operate['find_type2'] == ep.find_element_by_xpath or \
            operate['find_type2'] == ep.find_element_by_name or operate['find_type2'] == ep.find_element_by_class_name:
                    result = self.element_by2(operate).text
                elif operate['find_type2'] == ep.find_elements_by_id or operate['find_type2'] == ep.find_elements_by_xpath or \
            operate['find_type2'] == ep.find_elements_by_name or operate['find_type2'] == ep.find_elements_by_class_name:
                    result = self.element_by2(operate)[operate['index2']].text
                re_reulst = re.findall(r'[:.\-_a-zA-Z\d+\u4e00-\u9fa5]', result)
                text = ''.join(re_reulst)
                print('33333333333::::::::',text)
                if text == operate["find_v"]:
                    time.sleep(1)
                    return {'result': True}
                if time.time()-start_time > operate['find_time_out']:
                    return {'result': False}
    # 移动滚动条到某元素底部
    def move_scrollbar_bottom(self, operate):
        js2 = "arguments[0].scrollIntoView(false);"   #  false 底部对齐  true 顶部对齐 默认为true
        if operate['find_type'] == ep.find_element_by_id or operate['find_type'] == ep.find_element_by_xpath or \
            operate['find_type'] == ep.find_element_by_name or operate['find_type'] == ep.find_element_by_class_name:
            self.driver.execute_script(js2, self.element_by(operate))
            return {'result': True}
        elif operate['find_type'] == ep.find_elements_by_id or operate['find_type'] == ep.find_elements_by_xpath or \
            operate['find_type'] == ep.find_elements_by_name or operate['find_type'] == ep.find_elements_by_class_name:
            self.driver.execute_script(js2, self.element_by(operate)[operate['index']])
            return {'result': True}

    # 查找元素的封装
    def element_by2(self, operate):
        elements = {
            ep.find_element_by_id: lambda :self.driver.find_element_by_id(operate['element_info2']),
            ep.find_element_by_class_name: lambda :self.driver.find_element_by_class_name(operate['element_info2']),
            ep.find_element_by_name: lambda : self.driver.find_element_by_name(operate['element_info2']),
            ep.find_element_by_xpath: lambda : self.driver.find_element_by_xpath(operate['element_info2']),
            ep.find_elements_by_id: lambda: self.driver.find_elements_by_id(operate['element_info2']),
            ep.find_elements_by_class_name: lambda : self.driver.find_elements_by_class_name(operate['element_info2']),
            ep.find_elements_by_xpath: lambda: self.driver.find_elements_by_xpath(operate['element_info2']),
            ep.find_elements_by_name: lambda: self. driver.find_elements_by_name(operate['element_info2'])
        }
        return elements[operate['find_type2']]()

    # 查找元素的封装
    def element_by(self, operate):
        elements = {
            ep.find_element_by_id: lambda :self.driver.find_element_by_id(operate['element_info']),
            ep.find_element_by_class_name: lambda :self.driver.find_element_by_class_name(operate['element_info']),
            ep.find_element_by_name: lambda : self.driver.find_element_by_name(operate['element_info']),
            ep.find_element_by_xpath: lambda : self.driver.find_element_by_xpath(operate['element_info']),
            ep.find_elements_by_id: lambda: self.driver.find_elements_by_id(operate['element_info']),
            ep.find_elements_by_class_name: lambda : self.driver.find_elements_by_class_name(operate['element_info']),
            ep.find_elements_by_xpath: lambda: self.driver.find_elements_by_xpath(operate['element_info']),
            ep.find_elements_by_name: lambda: self. driver.find_elements_by_name(operate['element_info'])
        }
        return elements[operate['find_type']]()

if __name__=='__main__':
    from common.operate_yaml import getYam
    from common.Logger import myLog
    logTest = myLog.getLog("chrome")
    driver = webdriver.Chrome()
    driver.get('http://192.168.1.189:8515/#/login')
    oe = OperateElement(driver)
    path = os.path.dirname(os.getcwd()) + '\YAML\login\login'
    data = getYam(path)
    print(data)
    for i in data[1]['testcase']:
        oe.operate(i, data[1]['testinfo'], logTest)
        print(i['info'])
        # time.sleep(3)



