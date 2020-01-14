# -*- coding: utf-8 -*-

class ElementParam(object):

    # selenium 关键字
    find_element_by_id = 'id'
    find_element_by_class_name = 'class_name'
    find_element_by_name = 'name'
    find_element_by_xpath = 'xpath'
    find_elements_by_id = 'ids'
    find_elements_by_class_name = 'class_names'
    find_elements_by_xpath = 'xpaths'
    find_elements_by_name = 'names'
    WAIT_TIME = 20  # 查找元素等待时间
    CLICK = 'click'   # 点击事件
    SEND_KEYS = 'send_keys'  # 输入事件
    ACTION_CHAINS = 'action_chains'  # 鼠标悬停事件
    GET_TEXT = 'get_text'
    GET_VALUE = 'get_value'
    MOVE_BY_OFFSET = 'move_by_offset'  # 移动鼠标到某个像素
    GET_CURRENT_URL = 'get_current_url'
    GET_ATTR = 'get_attr'
    IS_DISPLAYED = "is_displayed"  # 检查元素是否显示
    FIND_DOWN = "find_down"  # 下拉菜单中向下查找元素
    MOVE_SCROLLBAR_BOTTOM = "move_scrollbar_bottom"  # 移动滚动条到某元素底部
    UPLOAD_FILE = "upload_file"  # 上传文件 使用autoit可执行文件
    DOWNLOAD_FILE = 'download_file' # 校验下载文件是否存在
    REFRESH_GET_TEXT = "refresh_get_text"  # 刷新页面获取数据
    REFRESH_GET_ATTR = "refresh_get_attr"  # 刷新页面获取属性
    TO_IFRAME = "to_iframe"  # 切换到iframe
    DEFAULT_CONTENT = "default_content"  # 从iframe 切换到当前
    REFRESH = "refresh"  # 刷新当前页面
    CLEAR = "clear"  # 清楚输入框
    TO_URL = "to_url"  # 跳转到某链接
    TO_WINDOW = "to_window"  # 切换到某个窗口
    CLOSE_WINDOW = "close_window"  # 关闭当前窗口
    DRAG_EL = "drag_el"  # 拖拽元素 到第二元素 或者 某个 像素
    DOUBLE_CLICK = "double_click"  # 双击
    KEY_OPETATE = "key_operate" # 键盘操作
    REFRESH_TIME_DIFFERENCE = "refresh_time_difference"  # 刷新页面直到时间差小于预期值
    REFRESH_GET_TEXT_IS_EXPECT = "refresh_get_text_is_expect"  # 刷新页面 获取的值符合预期 返回最后的text
    KEY_PAGE_DOWN ='key_page_down' #下滑 
    ZJ_CLICK='zj_click'#直接单击
    IS_SELECTED='is_selected'#判断勾选框


    # 错误日志
    TIME_OUT = "timeout"
    NO_SUCH = "noSuch"
    WEB_DROVER_EXCEPTION = "WebDriverException"
    INDEX_ERROR = "index_error"
    STALE_ELEMENT_REFERENCE_EXCEPTION = "StaleElementReferenceException"
    DEFAULT_ERROR = "default_error"
    VALUE_ERROR = "value_error"  # YAML给出的value不合法
    # URL_INEQUALITY_ERROR = "url_inequality_error"  # URL不相等错误

    # 检查点
    CONTRARY = "contrary"  # 相反检查点，表示如果检查元素存在就说明失败，如删除后，此元素依然存在
    DEFAULT_CHECK = "default_check"  # 默认检查点，查找页面元素是否存在
    VESSEL_CONTAIN_CURRENT = "vessel_contain_current"  # 容器  包含  当前值
    VESSEL_NOT_CONTAIN_CURRENT = "vessel_not_contain_current"  # 容器  不包含  当前值
    VESSEL_CONTAIN_EXPECT = "vessel_contain_expect"  # 容器 包含 预期值
    VESSEL_NOT_CONTAIN_EXPECT = "vessel_not_contain_expect"  # 容器 不包含 预期值
    CURRENT_CONTAIN_EXPECT = "current_contain_expect"  # 当前值 包含 预期值
    CURRENT_EQUAL_EXPECT = "current_equal_expect"  # 当前值 等于 预期值
    CURRENT_NOT_EQUAL_EXPECT = "current_not_equal_expect"  # 当前值 不等于 预期值

    DISPLAYED = "displayed"  # 检查元素显示
    NOT_DISPLAYED = "not_displayed"  # 检查元素不显示
    TIME_DIFFERENCE = 'time_difference'  # 检查时间差

    # 文件名字
    INFO_FILE = "info.pickle"
    SUM_FILE = "sum.pickle"
    REPORT_FILE = "Report.xlsx"

    # URL = 'http://192.168.1.81:8515/#/login'
    # HOST = 'http://192.168.1.81:8515'
    # #测试83环境
    URL = 'http://192.168.1.83:8515/#/login'
    HOST = 'http://192.168.1.83:8515'

    # 页面url
    #资源目录
    RESOURCE_MEN_URL = HOST + "/#/resourceMan"

    #采集器页面
    IMPORT_DATA_URL = HOST + "/#/collector/importData"  # 导入任务页
    VIEW_URL = HOST + "/#/collector/autoui83/view/10c7da46-8552-47cc-9b96-38b69a337ed5"  #采集器autoui83 详细信息页
    TASK_LIST_URL = HOST + "/#/collector/autoui83/taskList/10c7da46-8552-47cc-9b96-38b69a337ed5"  #采集器autoui83 任务列表页
    DIR_URL = HOST + "/#/collector/autoui83/dir/10c7da46-8552-47cc-9b96-38b69a337ed5"      #采集器autoui83 资源目录页

    # 数据监控
    OPERATIONAL_URL = HOST + "/#/hippo/index"  # 运维管控
    TASK_CONTROL_URL = HOST + "/#/hippo/taskControl"  # 任务监控

    # 质量分析
    EXECUTE_INFO_URL = HOST + "/#/qualityAnalysis/teInformation"   #  任务执行信息
    ANALYZE_TEMPLATE_URL = HOST + "/#/qualityAnalysis/analysisTemplate"  # 分析模板URL
    ANALYZE_RULES_URL = HOST + "/#/qualityAnalysis/analysisRules"   # 分析规则URL
    ER_STATISTICS_URL = HOST + "/#/qualityAnalysis/erStatistics"        # 评估结果统计

    # 血缘分析
    BLOOD_ANALYZE_URL = HOST + "/#/kinship/:id/"  # 血缘分析 url

    # 元数据分析
    SCHEMA_ANALYZE_URL = HOST + "/#/schemaAnalysis/:id/"   # 元数据分析 url

    # 数据分析
    FLOW_MANAGEMENT_URL = HOST + "/#/design"  # 流程管理 url



    #脚本版本
    VERSION = '2020-01-14'


