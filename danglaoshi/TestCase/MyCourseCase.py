# -*- coding:utf-8 -*-
from danglaoshi.Common import BaseMethod
import unittest
from danglaoshi.TestAction.Login_Test import LoginAction
from danglaoshi.Data.Elements.PositionMyCourse import PositionMyCourse
from danglaoshi.TestAction.Course_Test.CourseListAction import CourseListAction
from ddt import ddt, data, unpack
# import operator
import time


@ddt
class MyCourseCase(unittest.TestCase):
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

    my_course = PositionMyCourse()
    into_course_by_course_name = CourseListAction()

    def test_my_course_element_check(self):
        BaseMethod.click(elem_detail=self.my_course.foot_course)
        self.assertEqual(BaseMethod.is_exist(elem_detail=self.my_course.my_course), True)
        self.assertEqual(BaseMethod.is_exist(elem_detail=self.my_course.my_course_num), True)
        if BaseMethod.is_exist(elem_detail=self.my_course.my_course_guide):
            BaseMethod.click(elem_detail=self.my_course.my_course_guide)
        BaseMethod.click(elem_detail=self.my_course.my_course)
        if BaseMethod.is_exist(elem_detail=self.my_course.course_guide):
            BaseMethod.click(elem_detail=self.my_course.course_guide)
        #  time.sleep(1)
        self.assertEqual(BaseMethod.is_exist(elem_detail=self.my_course.get_my_course_whole(1), by="xpath", i=1), False)
        BaseMethod.click(elem_detail=self.my_course.my_course_back)

    def test_placed_at_the_top(self):
        BaseMethod.click(elem_detail=self.my_course.foot_course)
        self.assertEqual(BaseMethod.is_exist(elem_detail=self.my_course.my_course), True)
        self.assertEqual(BaseMethod.is_exist(elem_detail=self.my_course.my_course_num), True)
        if BaseMethod.is_exist(elem_detail=self.my_course.my_course_guide):
            BaseMethod.click(elem_detail=self.my_course.my_course_guide)
        BaseMethod.click(elem_detail=self.my_course.my_course)
        if BaseMethod.is_exist(elem_detail=self.my_course.course_guide):
            BaseMethod.click(elem_detail=self.my_course.course_guide)
        # self.into_course_by_course_name.click_course("测试混合直播")
        BaseMethod.swipe_on(direction="left", t=200)

    def test_delete_allow_course(self):
        pass

    def test_delete_ban_course(self):
        pass

    def test_cancel_top_course(self):
        pass

    def test_expired_course(self):
        pass


if __name__ == '__main__':
    unittest.main()
