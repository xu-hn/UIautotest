# -*- coding: utf-8 -*-

import logging
import os, time
import threading

PATH = lambda p:  os.path.abspath(
        os.path.join(os.path.dirname(__file__), p))

class Log:

    def __init__(self, name):
        global resultPath, log_path  # 创建三个全局变量
        resultPath = PATH("../log")
        log_path = resultPath + '/' + name + time.strftime('%Y%m%d_%H%M%S', time.localtime())
        if not os.path.exists(log_path):
            os.mkdir(log_path)

        self.checkNo = 0
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

        file_h = logging.FileHandler(os.path.join(log_path, 'out_put.log'), encoding='utf-8')
        formatter = logging.Formatter('%(asctime)s  - %(levelname)s - %(message)s')
        file_h.setFormatter(formatter)

        stream_h = logging.StreamHandler()
        stream_h.setFormatter(formatter)
        self.logger.addHandler(stream_h)

        self.logger.addHandler(file_h)

    def buildStartLine(self, caseNo):
        """build the start log
        :param caseNo:
        :return:
        """
        startLine = "----  " + caseNo + "   " + "   " + \
                    "  ----"
        # startLine = "----  " + caseNo + "   " + "START" + "   " + \
        #             "  ----"
        self.logger.info(startLine)

    def printer(self, text):
        self.logger.info(text)

    def checkPointOK(self, caseName, checkPoint):
        self.checkNo += 1
        self.logger.info("[CheckPoint_" + str(self.checkNo) + "]: " + checkPoint + ": OK")
        print("==用例_%s检查点成功==" % caseName)

    def checkPointNG(self, driver, caseName, checkPoint):

        self.checkNo += 1

        self.logger.info("[CheckPoint_" + str(self.checkNo) + "]: " + checkPoint + ": NG")
        # take shot
        return self.screenshotNG(driver, caseName)

    def screenshotNG(self, driver, caseName):
        # screenshotPath = os.path.join(log_path, caseName)
        screenshotName = "CheckPoint_" + str(self.checkNo)+ '__' + caseName+ "__NG.png"
        # wait for animations to complete before taking screenshot
        time.sleep(1)
        print(log_path)
        print(os.path.join(log_path, screenshotName))
        driver.get_screenshot_as_file(os.path.join(log_path, screenshotName))
        time.sleep(1)
        return os.path.join(log_path, screenshotName)

    def checkPoint_false_cancel(self):
        # case失败重跑前取消
        self.checkNo -= 1

class myLog:
    """
    This class is used to get log
    """

    log = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def getLog(devices):
        if myLog.log is None:
            myLog.mutex.acquire()
            myLog.log = Log(devices)
            myLog.mutex.release()

        return myLog.log

if __name__ == "__main__":
    logTest = myLog.getLog("devices")
    # logger = logTest.getMyLogger()
    logTest.buildStartLine("开始")





