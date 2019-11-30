# 封装基本方法
import time
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

import os
import threading
# 全局变量driver
driver = None


# 与app创建连接（noReset设置为True表示从跳过初始引导页）
def driver_open(boolean=True):
    desired_caps = {
        "platformName": "Android",
        "platformVersion": "4.4.2",
        "deviceName": "Android Emulator",
        "appPackage": "com.ruicheng.teacher",
        "appActivity": "com.ruicheng.teacher.Activity.SplashActivity",
        "noReset": boolean,
        # 处理无法输入中文的问题
        'unicodeKeyboard': True,  # 使用unicodeKeyboard的编码方式来发送字符串
        'resetKeyboard': True  # 将键盘给隐藏起来
    }
    global driver
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


# 关闭driver
def driver_close():
    driver.quit()


# 定位元素
def find_elem(by, elem_detail, i):
    elem = ''
    if by == 'id':
        elem = driver.find_element_by_id(elem_detail)
    elif by == 'ids':
        elem = driver.find_elements_by_id(elem_detail)[i]
    elif by == 'class':
        elem = driver.find_elements_by_class_name(elem_detail)[i]
    elif by == 'xpath':
        elem = driver.find_elements_by_xpath(elem_detail)[i]
    return elem


# 输入
def send(elem_detail, value, by='id', i=0):
    elem = find_elem(by, elem_detail, i)
    elem.send_keys(value)


# 通过id输入
# def send(elem_id, value):
#     elem = driver.find_element_by_id(elem_id)
#     elem.send_keys(value)


# 点击
def click(elem_detail, by='id', i=0):
    elem = find_elem(by, elem_detail, i)
    elem.click()


# 通过id点击
# def click(elem_id):
#     elem = driver.find_element_by_id(elem_id)
#     elem.click()


# 通过xpath点击
def click_xpath(xpath):
    elem = driver.find_elements_by_xpath(xpath)
    elem[0].click()


# 暂停s秒
def sleep(s):
    time.sleep(s)


# 获取屏幕大小
def get_screen_size():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return x, y


# 向上滑动屏幕(t为滑动时间，单位：ms)
def swipe_up(t):
    screen = get_screen_size()
    driver.swipe(screen[0] * 0.5, screen[1] * 0.75, screen[0] * 0.5, screen[1] * 0.25, t)


# 向下滑动屏幕(t为滑动时间，单位：ms)
def swipe_down(t):
    screen = get_screen_size()
    driver.swipe(screen[0] * 0.5, screen[1] * 0.25, screen[0] * 0.5, screen[1] * 0.75, t)


# 向左滑动屏幕(t为滑动时间，单位：ms)
def swipe_left(t):
    screen = get_screen_size()
    driver.swipe(screen[0] * 0.75, screen[1] * 0.5, screen[0] * 0.25, screen[1] * 0.5, t)


# 向右滑动屏幕(t为滑动时间，单位：ms)
def swipe_right(t):
    screen = get_screen_size()
    driver.swipe(screen[0] * 0.25, screen[1] * 0.5, screen[0] * 0.75, screen[1] * 0.5, t)


# 向上滑动屏幕--为性别量身定做(t为滑动时间，单位：ms)
def swipe_up_sex(t=600):
    screen = get_screen_size()
    driver.swipe(screen[0] * 0.5, screen[1] * 0.98, screen[0] * 0.5, screen[1] * 0.88, t)


# 滑动屏幕
def swipe_on(direction, t=300):
    if direction == 'up':
        swipe_up(t)
    elif direction == 'down':
        swipe_down(t)
    elif direction == 'left':
        swipe_left(t)
    elif direction == 'right':
        swipe_right(t)


# 截图(返回保存位置)
def screen_shot():
    img_path = os.path.join(os.getcwd(), 'screenshots')
    now = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime(time.time()))
    image_path = os.path.join(img_path, "img_" + now + ".png")
    print(driver.get_screenshot_as_file(image_path))
    return image_path


# 判断元素是否存在
def is_exist(elem_detail, by='id', i=0):
    try:
        find_elem(by, elem_detail, i).is_displayed()
        exist = True
    except Exception as error:
        exist = False
        print(error)
    return exist


# 每秒判断一次元素是否存在,持续十秒，十秒后结束
# 返回状态：0：等待，1：存在，2：不存在）
exec_count = 0


def is_exist_wait(elem_detail, by='id', i=0):
    global exec_count
    try:
        find_elem(by, elem_detail, i).is_displayed()
        exec_count = 0
        return 1
    except Exception as error:
        exec_count += 1
        if exec_count < 10:
            threading.Timer\
                (1, is_exist_wait(elem_detail, by, i)).start()
            print('wait------')
            return 0
        else:
            exec_count = 0
            print(error)
            return 2


# 依据id判断元素是否存在
# def is_exist(elem_id):
#     try:
#         driver.find_element_by_id(elem_id).is_displayed()
#         exist = True
#     except Exception as error:
#         exist = False
#         print(error)
#     return exist

def is_exist_text(elem_text):
    try:
        driver.find_element_by_text(elem_text).is_displayed()
        exist = True
    except Exception as error:
        exist = False
        print(error)
    return exist


# 依据xpath判断元素是否存在
def is_exist_xpath(xpath):
    try:
        driver.find_elements_by_xpath(xpath)[0].is_displayed()
        exist = True
    except Exception as error:
        exist = False
        print(error)
    return exist


# 获取当前activity
def current_activity():
    activity = driver.current_activity
    return activity


# 跳转activity
def to_activity(activity):
    driver.start_activity(app_package="com.ruicheng.teacher", app_activity=activity)


# 获取text
def get_text(elem_detail, by='id', i=0):
    text = find_elem(by, elem_detail, i).text
    return text


# 通过id获取text
# def get_text(elem_id):
#     text = driver.find_element_by_id(elem_id).text
#     return text


# 通过xpath获取text
def get_text_xpath(xpath):
    elem = driver.find_elements_by_xpath(xpath)
    elem_text = elem[0].text
    return elem_text


# 判断是否存在包含msg的toast消息
def is_toast(msg):
    try:
        WebDriverWait(driver, 10).until(expected_conditions.
                                        presence_of_all_elements_located((By.PARTIAL_LINK_TEXT, msg)))
        result = True
    except Exception as error:
        print(error)
        result = False
    return result


# 获取当前页的url地址
def get_url():
    url = ""
    return url


# 切换fragment
def to_fragment():
    pass


# 通过坐标点击
def tap_test(x, y):
    # 获取当前手机屏幕大小X,Y
    x1 = driver.get_window_size()['width']
    y1 = driver.get_window_size()['height']
    # 设定系数,控件在当前手机的坐标位置除以当前手机的最大坐标就是相对的系数了
    a1 = x/x1
    b1 = y/y1
    # 屏幕坐标乘以系数即为用户要点击位置的具体坐标
    driver.tap([(a1*x1, b1*y1)], 100)
