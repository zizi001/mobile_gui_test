# -*- coding:utf-8 -*-
from danglaoshi.Common import BaseMethod
import unittest
from danglaoshi.TestAction.Login_Test import LoginAction
from danglaoshi.Data.Elements.PositionTryToLearn import PositionTryToLearn
from danglaoshi.TestAction.Course_Test.CourseListAction import CourseListAction
from ddt import ddt, data, unpack
# import operator
import time


@ddt
class TryToLearnCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        BaseMethod.driver_open(True)
        LoginAction.login_out()
        LoginAction.login("15769270635", "123456")
        LoginAction.after_login()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        LoginAction.login_out()
        BaseMethod.driver_close()

    try_to_learn = PositionTryToLearn()
    into_course_by_course_name = CourseListAction()

    def test_try_to_learn_list_check(self):
        BaseMethod.click(elem_detail=self.try_to_learn.foot_course)
        if BaseMethod.is_exist(elem_detail=self.try_to_learn.my_course_guide):
            BaseMethod.click(elem_detail=self.try_to_learn.my_course_guide)
        self.into_course_by_course_name.click_course("试听课程测试")
        print("进入课程成功")
        BaseMethod.click(self.try_to_learn.try_to_learn_button)
        self.assertEqual(BaseMethod.is_exist(elem_detail=self.try_to_learn.get_try_to_learn_list(1), by="xpath"), True)
    # 试学列表为1--直接播放
    #     print(self.try_to_learn.get_try_to_learn_list(1).__len__())
    # 试学列表>1--展示列表 选择播放
    #     BaseMethod.click(elem_detail=self.try_to_learn.get_try_to_learn_list(1), by="xpath", i=0)
    #     self.assertEqual(BaseMethod.is_exist(elem_detail=self.try_to_learn.try_to_learn_send), True)

    # 后续补充

    def test_into_try_to_learn(self):
        pass

    def test_into_try_to_learn_playback(self):
        pass

    def test_sliding_try_to_learn_list(self):
        pass

    def test_one_try_to_learn_lesson(self):
        pass

    def test_multiple_try_to_learn_lesson(self):
        pass


if __name__ == '__main__':
    unittest.main()
