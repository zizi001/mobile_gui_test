# -*- coding:utf-8 -*-
from danglaoshi.Common import BaseMethod
import unittest
from danglaoshi.TestAction.Login_Test import LoginAction
from danglaoshi.Data.Elements.PositionCourseSpecifications import PositionCourseSpecifications
from danglaoshi.TestAction.Course_Test.CourseListAction import CourseListAction
from ddt import ddt, data, unpack
# import operator
import time


@ddt
class CourseSpecificationsCase(unittest.TestCase):
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

    course_specifications = PositionCourseSpecifications()
    into_course_by_course_name = CourseListAction()

    def test_my_course_specifications_element_check(self):
        BaseMethod.click(elem_detail=self.course_specifications.foot_course)
        if BaseMethod.is_exist(elem_detail=self.course_specifications.my_course_guide):
            BaseMethod.click(elem_detail=self.course_specifications.my_course_guide)
        self.into_course_by_course_name.click_course("H5测试购买")
        print("进入课程成功")
        self.assertEqual(BaseMethod.is_exist(elem_detail=self.course_specifications.choose_specifications), True)
        self.assertEqual(BaseMethod.is_exist(elem_detail=self.course_specifications.choose_specifications_arrow), True)

        BaseMethod.click(elem_detail=self.course_specifications.back_key)

    def test_choice_specifications(self):
        pass

    def test_switch_specifications(self):
        pass

    def test_after_submit_specifications(self):
        pass


if __name__ == '__main__':
    unittest.main()
