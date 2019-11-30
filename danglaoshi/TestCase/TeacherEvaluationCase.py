# -*- coding:utf-8 -*-
from danglaoshi.Common import BaseMethod
import unittest
from danglaoshi.TestAction.Login_Test import LoginAction
from danglaoshi.Data.Elements.PositionTeacherEvaluation import PositionTeacherEvaluation
from danglaoshi.TestAction.Course_Test.CourseListAction import CourseListAction
from ddt import ddt, data, unpack
# import operator
import time


@ddt
class TeacherEvaluationCase(unittest.TestCase):
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

    teacher_evaluation = PositionTeacherEvaluation()
    into_course_by_course_name = CourseListAction()

    def test_teacher_evaluation_element_check(self):
        BaseMethod.click(elem_detail=self.teacher_evaluation.foot_course)
        self.into_course_by_course_name.click_course("试听课程测试")
        self.assertEqual(BaseMethod.is_exist(elem_detail=self.teacher_evaluation.get_all_evaluation(1), by="xpath"),
                         False)

    def test_total_teacher_evaluation(self):
        pass

    def test_teacher_evaluation_score(self):
        pass

    def test_teacher_evaluation_stars(self):
        pass

    def test_teacher_evaluation_content(self):
        pass

    def test_teacher_evaluation_introduction(self):
        pass

    def test_teacher_evaluation_img(self):
        pass

    def test_teacher_evaluation_user(self):
        pass

    def test_teacher_evaluation_time(self):
        pass


if __name__ == '__main__':
    unittest.main()
