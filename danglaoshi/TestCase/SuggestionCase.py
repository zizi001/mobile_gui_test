# -*- coding:utf-8 -*-
from danglaoshi.Common import BaseMethod
import unittest
# from danglaoshi.Data.Elements import PositionSetting
from danglaoshi.TestAction.Login_Test import LoginAction
from danglaoshi.Data.Elements.PositionSetting import PositionSetting
from ddt import ddt, data, unpack
import operator
import time


@ddt
class SuggestionCase(unittest.TestCase):
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

    feedback = PositionSetting()

    def test_suggestion_element_check(self):
        BaseMethod.click(elem_detail=PositionSetting.user_center)
        BaseMethod.swipe_on("up", 1000)
        BaseMethod.click(elem_detail=self.feedback.ll_setting)
        BaseMethod.click(elem_detail=self.feedback.rl_feedback)
        actual1 = (BaseMethod.is_exist(elem_detail=self.feedback.feedback_title)) and \
                  (operator.eq(BaseMethod.get_text(elem_detail=self.feedback.feedback_title), "意见反馈"))
        actual2 = (BaseMethod.is_exist(elem_detail=self.feedback.feedback_content)) and \
                  (BaseMethod.is_exist(elem_detail=self.feedback.feedback_submit))
        actual3 = operator.eq(BaseMethod.get_text(elem_detail=self.feedback.feedback_content), "详细描述您的问题，字数控制在10～500以内")
        actual4 = BaseMethod.is_exist(elem_detail=self.feedback.feedback_back)
        if (actual1 is True) and (actual2 is True) and (actual3 is True) and (actual4 is True):
            print("意见反馈页面元素检查完毕,over")
            pass
        BaseMethod.click(elem_detail=self.feedback.feedback_back)
        BaseMethod.click(elem_detail=self.feedback.setting_back)

    def test_canal_suggestion_content(self):
        BaseMethod.click(elem_detail=PositionSetting.user_center)
        BaseMethod.swipe_on("up", 1000)
        BaseMethod.click(elem_detail=self.feedback.ll_setting)
        BaseMethod.click(elem_detail=self.feedback.rl_feedback)
        BaseMethod.click(elem_detail=self.feedback.feedback_content)
        BaseMethod.send(elem_detail=self.feedback.feedback_content, value="我是来给你们提意见的,怕不怕我是来给你们提意见的,怕不怕我是来给你们提意见的,怕不怕", by="id")
        time.sleep(1)
        BaseMethod.click(elem_detail=self.feedback.feedback_submit)
        time.sleep(0.2)
        # self.assertEquals(BaseMethod.is_exist(elem_detail=self.feedback.after_submit), True)
        self.assertEqual(BaseMethod.get_text(elem_detail=self.feedback.after_submit), "提交成功，感谢您的反馈，小的会尽快处理 。")
        # self.assertEquals(operator.eq(BaseMethod.get_text(elem_detail=self.feedback.after_submit),
        # "提交成功，感谢您的反馈，小的会尽快处理 。"), True)
        BaseMethod.click(elem_detail=self.feedback.md_buttonDefaultNegative)
        if BaseMethod.is_exist(elem_detail=self.feedback.feedback_submit):
            print("取消反馈")
        else:
            print("取消反馈失败")
        time.sleep(1)
        BaseMethod.click(elem_detail=self.feedback.feedback_back)
        BaseMethod.click(elem_detail=self.feedback.setting_back)

    def test_confirm_suggestion_content(self):
        BaseMethod.click(elem_detail=self.feedback.user_center)
        BaseMethod.swipe_on("up", 1000)
        BaseMethod.click(elem_detail=self.feedback.ll_setting)
        BaseMethod.click(elem_detail=self.feedback.rl_feedback)
        BaseMethod.click(elem_detail=self.feedback.feedback_content)
        BaseMethod.send(elem_detail=self.feedback.feedback_content, value="我是来给你们提意见的,一定得提交", by="id")
        BaseMethod.click(elem_detail=self.feedback.feedback_submit)
        self.assertEquals(BaseMethod.is_exist(elem_detail=self.feedback.after_submit), True)
        self.assertEqual(BaseMethod.get_text(elem_detail=self.feedback.after_submit), "提交成功，感谢您的反馈，小的会尽快处理 。")
        BaseMethod.click(elem_detail=self.feedback.md_buttonDefaultPositive)
        time.sleep(0.2)
        actual3 = self.assertEquals(BaseMethod.is_exist(elem_detail=self.feedback.rl_feedback), True)
        if actual3 is True:
            print("反馈提交成功")
        else:
            print("反馈提交失败")
        BaseMethod.click(elem_detail=self.feedback.setting_back)


if __name__ == '__main__':
    unittest.main()
