#!/usr/bin/python3
# coding=utf-8
from appium import webdriver
from danglaoshi.Data.Elements import PositionLogin

# 通过APPium对APP进行初始化操作
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '21'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'com.ruicheng.teacher'
desired_caps['appActivity'] = '.Activity.SplashActivity'
desired_caps['unicodeKeyboard'] = 'True'
desired_caps['resetKeyboard'] = 'True'
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
# driver相当于获取到了一个操作当前APP的一个实例

'''
api_req = ApiRequest()
params = {'telephone': '15769270635'}
result = api_req.api_req('user/checkPhone', params)
if result['data']['exist']:
    pass
'''

username = driver.find_element_by_id(PositionLogin.PositionLogin.username)
username.send_keys("15769270635")

driver.find_element_by_id("com.ruicheng.teacher:id/bt_login").click()
pwd = driver.find_element_by_id("com.ruicheng.teacher:id/pswRelativelayout")
pwd.send_keys("123456")
driver.find_element_by_id("com.ruicheng.teacher:id/bt_login").click()

# driver.current_activity()


driver.find_element_by_id("com.ruicheng.teacher:id/tv_practice").click()
driver.find_element_by_id("com.ruicheng.teacher:id/tv_course_name").click()
driver.find_element_by_id("com.ruicheng.teacher:id/tv_open").click()


def practice_test():
    driver.find_element_by_id("com.ruicheng.teacher:id/rb_btnB").click()
    driver.find_element_by_id("com.ruicheng.teacher:id/rb_btnA").click()
    driver.find_element_by_id("com.ruicheng.teacher:id/rb_btnC").click()
    driver.find_element_by_id("com.ruicheng.teacher:id/rb_btnD").click()
    driver.find_element_by_id("com.ruicheng.teacher:id/rb_btnA").click()
    driver.find_element_by_id("com.ruicheng.teacher:id/rb_btnB").click()
    driver.find_element_by_id("com.ruicheng.teacher:id/rb_btnD").click()
    driver.find_element_by_id("com.ruicheng.teacher:id/rb_btnB").click()
    driver.find_element_by_id("com.ruicheng.teacher:id/rb_btnC").click()
    driver.find_element_by_id("com.ruicheng.teacher:id/rb_btnB").click()
    driver.find_element_by_id("com.ruicheng.teacher:id/rb_btnD").click()
    driver.find_element_by_id("com.ruicheng.teacher:id/rb_btnB").click()
    driver.find_element_by_id("com.ruicheng.teacher:id/rb_btnC").click()
    driver.find_element_by_id("com.ruicheng.teacher:id/rb_btnB").click()
    driver.find_element_by_id("com.ruicheng.teacher:id/rb_btnA").click()


practice_test()


driver.quit()
