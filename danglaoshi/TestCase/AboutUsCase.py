# -*- coding:utf-8 -*-
from danglaoshi.Common import BaseMethod
import unittest
# from danglaoshi.Data.Elements import PositionSetting
from danglaoshi.TestAction.Login_Test import LoginAction
from danglaoshi.Data.Elements.PositionSetting import PositionSetting
from ddt import ddt, data, unpack
# import operator
import time


@ddt
class AboutUsCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        BaseMethod.driver_open(True)
        LoginAction.login_out()
        LoginAction.login("13100000266", "123456")
        LoginAction.after_login()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        LoginAction.login_out()
        BaseMethod.driver_close()

    about_us = PositionSetting()

    def test_about_us_logo_element_check(self):
        BaseMethod.click(elem_detail=self.about_us.user_center)
        BaseMethod.swipe_on("up", 1000)
        BaseMethod.click(elem_detail=self.about_us.ll_setting)
        BaseMethod.click(elem_detail=self.about_us.rl_about_us)
        self.assertEqual(BaseMethod.is_exist(elem_detail=self.about_us.get_danglaoshi_logo(1), by="xpath", i=1), False)
        time.sleep(1)
        BaseMethod.click(elem_detail=self.about_us.about_us_back)
        BaseMethod.click(elem_detail=self.about_us.setting_back)

    def test_about_us_version_element_check(self):
        BaseMethod.click(elem_detail=self.about_us.user_center)
        BaseMethod.swipe_on("up", 1000)
        BaseMethod.click(elem_detail=self.about_us.ll_setting)
        BaseMethod.click(elem_detail=self.about_us.rl_about_us)
        self.assertEqual(BaseMethod.get_text(elem_detail=self.about_us.tv_version), "当老师: v3.1.1")
        BaseMethod.click(elem_detail=self.about_us.about_us_back)
        BaseMethod.click(elem_detail=self.about_us.setting_back)

    def test_about_us_wechat_element_check(self):
        BaseMethod.click(elem_detail=self.about_us.user_center)
        BaseMethod.swipe_on("up", 1000)
        BaseMethod.click(elem_detail=self.about_us.ll_setting)
        BaseMethod.click(elem_detail=self.about_us.rl_about_us)
        self.assertEqual(BaseMethod.is_exist(elem_detail=self.about_us.get_official_msg(3), by="xpath", i=3), False)
        # self.assertEqual(BaseMethod.get_text(elem_detail=self.about_us.official_wechat_nick, by="xpath"),
        #  "danglaoshi123")
        BaseMethod.click(elem_detail=self.about_us.about_us_back)
        BaseMethod.click(elem_detail=self.about_us.setting_back)

    def test_about_us_webo_element_check(self):
        BaseMethod.click(elem_detail=self.about_us.user_center)
        BaseMethod.swipe_on("up", 1000)
        BaseMethod.click(elem_detail=self.about_us.ll_setting)
        BaseMethod.click(elem_detail=self.about_us.rl_about_us)
        self.assertEqual(BaseMethod.is_exist(elem_detail=self.about_us.get_official_msg(2), by="xpath", i=2), False)
        # self.assertEqual(BaseMethod.get_text(elem_detail=self.about_us.official_weibo_nick, by="xpath"), "@当老师APP")
        BaseMethod.click(elem_detail=self.about_us.about_us_back)
        BaseMethod.click(elem_detail=self.about_us.setting_back)

    def test_about_us_web_element_check(self):
        BaseMethod.click(elem_detail=self.about_us.user_center)
        BaseMethod.swipe_on("up", 1000)
        BaseMethod.click(elem_detail=self.about_us.ll_setting)
        BaseMethod.click(elem_detail=self.about_us.rl_about_us)
        self.assertEqual(BaseMethod.is_exist(elem_detail=self.about_us.get_official_msg(3), by="xpath", i=3), False)
        self.assertEqual(BaseMethod.get_text(elem_detail=self.about_us.official_website_url), "danglaoshi.net")
        BaseMethod.click(elem_detail=self.about_us.about_us_back)
        BaseMethod.click(elem_detail=self.about_us.setting_back)

    def test_about_us_copyrigth_element_check(self):
        BaseMethod.click(elem_detail=self.about_us.user_center)
        BaseMethod.swipe_on("up", 1000)
        BaseMethod.click(elem_detail=self.about_us.ll_setting)
        BaseMethod.click(elem_detail=self.about_us.rl_about_us)
        self.assertEqual(BaseMethod.is_exist(elem_detail=self.about_us.get_danglaoshi_rights(2),
                                             by="xpath", i=2), False)
        time.sleep(1)
        BaseMethod.click(elem_detail=self.about_us.about_us_back)
        BaseMethod.click(elem_detail=self.about_us.setting_back)


if __name__ == '__main__':
    unittest.main()
