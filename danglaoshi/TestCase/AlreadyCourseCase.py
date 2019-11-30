# -*- coding: UTF-8 -*-
# 课程详情操作
from danglaoshi.Common import BaseMethod
import unittest
from danglaoshi.Data.Elements.PositionCurriculum1 import PositionCurriculum1
from danglaoshi.TestAction.Login_Test import LoginAction
from danglaoshi.TestAction.Course_Test import CourseListAction
from danglaoshi.Data.Elements.PositionPurchaseCourse import PositionPurchase


class AlreadyCourseCase(unittest.TestCase):
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
    def test_AlreadyCourse1(self):
        BaseMethod.click(PositionCurriculum1.curriculum1)
        BaseMethod.click(PositionCurriculum1.curriculum_guidance)
        BaseMethod.sleep(2)
        self.assertEqual(BaseMethod.get_text(elem_detail=PositionCurriculum1.my_course1, by="id"), "我的课程", "错了")
        print(BaseMethod.get_text(elem_detail=PositionCurriculum1.my_course1, by="id"))

    # 点击课程
    def test_AlreadyCourse2(self):
        course_list_action = CourseListAction.CourseListAction()
        course_list_action.click_course(course_name="陕西招教备考指导")
        BaseMethod.sleep(2)
        course_list_action.click_course(course_name="陕西省教师招聘备考指导-自动化测试专用勿动！")
        BaseMethod.sleep(2)

    # 点课程购买
    def test_AlreadyCourse3(self):
        if BaseMethod.get_text(PositionCurriculum1.purchase_text) == "已购买":
            BaseMethod.click(PositionCurriculum1.look_course)
            BaseMethod.sleep(3)
        else:
            BaseMethod.click(PositionCurriculum1.look_course)
            BaseMethod.sleep(3)
            BaseMethod.click(PositionCurriculum1.get_course)
            BaseMethod.sleep(3)
            BaseMethod.click(PositionCurriculum1.see_course)

    # 加入qq群操作
    def test_AlreadyCourse4(self):
        BaseMethod.click(PositionPurchase.join_groups)
        BaseMethod.sleep(10)
        self.assertEqual(BaseMethod.get_text_xpath(PositionPurchase.qq_groups), "2017陕西招教做题群2")
        BaseMethod.click(PositionPurchase.qq_back)
        BaseMethod.sleep(3)
        BaseMethod.click(PositionCurriculum1.course_back)
        BaseMethod.click(PositionCurriculum1.course_back1)

    # 课程日历
    def test_AlreadyCourse5(self):
        BaseMethod.click(PositionCurriculum1.my_course1)
        BaseMethod.click(PositionPurchase.my_course_guidance)
        BaseMethod.sleep(3)
        BaseMethod.click(PositionPurchase.course_calendar)
        BaseMethod.sleep(3)
        self.assertEqual(BaseMethod.get_text(PositionPurchase.calendar_bt), "今日课程")
        BaseMethod.tap_test(x=361, y=401)
        self.assertEqual(BaseMethod.get_text(PositionPurchase.calendar_ks), "自动化测试劵")
        BaseMethod.click(PositionPurchase.calendar_back)

    # 我的课程界面判断
    def test_AlreadyCourse6(self):
        BaseMethod.swipe_down(300)
        BaseMethod.is_exist_text(elem_text="陕西省教师招聘备考指导-自动化测试专用勿动！")

    @classmethod
    def tearDownClass(cls):
        LoginAction.login_out()
        BaseMethod.driver_close()


if __name__ == '__main__':
    unittest.main()
