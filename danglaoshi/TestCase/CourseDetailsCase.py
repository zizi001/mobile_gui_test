# -*- coding: UTF-8 -*-
# 课程详情操作
from danglaoshi.Common import BaseMethod
import unittest
from danglaoshi.Data.Elements.PositionCurriculum1 import PositionCurriculum1
from danglaoshi.TestAction.Login_Test import LoginAction
from danglaoshi.TestAction.Course_Test import CourseListAction


class CourseDetailsCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        BaseMethod.driver_open(True)
        LoginAction.login("13100000998", "123456")
        LoginAction.after_login()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # 点击进入课程页
    def test_CourseDetails1(self):
        BaseMethod.click(PositionCurriculum1.curriculum1)
        BaseMethod.click(PositionCurriculum1.curriculum_guidance)
        BaseMethod.sleep(2)
        self.assertEqual(BaseMethod.get_text(elem_detail=PositionCurriculum1.course_screening, by="id"), "筛选", "错了")
        print(BaseMethod.get_text(elem_detail=PositionCurriculum1.course_screening, by="id"))

    # 点击筛选判断
    def test_CourseDetails2(self):
        BaseMethod.click(PositionCurriculum1.course_screening)
        BaseMethod.sleep(3)
        BaseMethod.tap_test(x=109, y=166)
        BaseMethod.sleep(3)
        BaseMethod.click(PositionCurriculum1.course_screening)
        BaseMethod.sleep(3)
        BaseMethod.tap_test(x=342, y=163)
        BaseMethod.sleep(10)

    # 点课程组课程
    def test_CourseDetails3(self):
        course_list_action = CourseListAction.CourseListAction()
        course_list_action.click_course(course_name="陕西招教备考指导")
        BaseMethod.sleep(2)
        course_list_action.click_course(course_name="陕西省教师招聘备考指导-自动化测试专用勿动！")
        BaseMethod.sleep(2)

    # 课程详情
    def test_CourseDetails4(self):
        BaseMethod.swipe_up(300)
        self.assertEqual(BaseMethod.get_text(elem_detail=PositionCurriculum1.course_introduction, by="id"), "课程介绍")

    # 老师简介
    def test_CourseDetails5(self):
        BaseMethod.click(PositionCurriculum1.teacher_show)
        BaseMethod.swipe_up(300)
        BaseMethod.sleep(3)
        self.assertEqual(BaseMethod.get_text(elem_detail=PositionCurriculum1.teacher_name, by="xpath"), "小雨考官01")
        print(BaseMethod.get_text(elem_detail=PositionCurriculum1.teacher_name, by="xpath"))

        # 进入课程
    def test_CourseDetails6(self):
        if BaseMethod.get_text(PositionCurriculum1.purchase_text) == "已购买":
            BaseMethod.click(PositionCurriculum1.look_course)
            BaseMethod.sleep(3)
        else:
            BaseMethod.click(PositionCurriculum1.look_course)
            BaseMethod.sleep(3)
            BaseMethod.click(PositionCurriculum1.get_course)
            BaseMethod.sleep(3)
            BaseMethod.click(PositionCurriculum1.see_course)

    # 进入评价
    def test_CourseDetails7(self):
        BaseMethod.click(PositionCurriculum1.play_back)
        BaseMethod.click(PositionCurriculum1.evaluation1, i=0)
        self.assertEqual(BaseMethod.get_text(elem_detail=PositionCurriculum1.evaluation1_title, by="id"), "评价")
        BaseMethod.click(PositionCurriculum1.edit_evaluation)
        BaseMethod.sleep(3)
        self.assertEqual(BaseMethod.get_text(elem_detail=PositionCurriculum1.eva_submission, by="id"), "提交")

    # 提交评价数据
    def test_CourseDetails8(self):
        BaseMethod.send(elem_detail=PositionCurriculum1.evaluation_content, value="这个课程讲的棒棒的", by="id")
        BaseMethod.click(PositionCurriculum1.stars_stars)
        BaseMethod.sleep(3)
        BaseMethod.click(PositionCurriculum1.eva_submission)

    # # 返回至课程列表
    # def test_CourseDetails9(self):
    #     BaseMethod.click(PositionCurriculum1.course_back)
    #     BaseMethod.click(PositionCurriculum1.course_back1)

    @classmethod
    def tearDownClass(cls):
        LoginAction.login_out()
        BaseMethod.driver_close()


if __name__ == '__main__':
    unittest.main()
