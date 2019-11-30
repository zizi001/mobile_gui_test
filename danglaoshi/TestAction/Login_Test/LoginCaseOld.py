# usr/bin/python
# encoding:utf-8
import time
from appium import webdriver
import unittest
from ddt import ddt, data, unpack
from danglaoshi.Data.Elements import PositionLogin


@ddt
class MyTestCase(unittest.TestCase):
    def setUp(self):
        print("setUp")
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '21'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['appPackage'] = 'com.ruicheng.teacher'
        desired_caps['appActivity'] = '.Activity.SplashActivity'
        # self.desired_caps['automationName'] = 'Selendroid'  # 相对于native_app多了这一个配置项
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

    @data(("15769270635", "123456789", True), ("13100000125", "123456", True), (" ", "123456", False))
    @unpack
    def testLogIn(self, username, password, expected_result):
        self.driver.find_element_by_id(PositionLogin.PositionLogin.username).send_keys(username)
        self.driver.find_element_by_id(PositionLogin.PositionLogin.bt_login).click()
        self.driver.find_element_by_id(PositionLogin.PositionLogin.password).send_keys(password)

        # try:
        #     if self.driver.find_element_by_id(PositionLogin.PositionLogin.bt_login).is_displayed():
        #         exist = True
        # except Exception as e:
        #     exist = False
        # self.assertEqual(exist, expected_result)
        self.assertEqual(self.driver.find_element_by_id(PositionLogin.PositionLogin.bt_login).is_displayed(),
                         expected_result)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
